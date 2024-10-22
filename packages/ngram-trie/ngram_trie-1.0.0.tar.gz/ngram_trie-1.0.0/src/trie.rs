pub mod trienode;
pub mod smoothing;

use trienode::TrieNode;
use smoothing::Smoothing;
use serde::{Serialize, Deserialize};
use std::mem;
use std::fs::{File, metadata};
use std::io::{BufReader, BufWriter};
use std::time::Instant;
use std::sync::Arc;
use std::ops::Range;
use bincode::{serialize_into, deserialize_from};
use tqdm::tqdm;
use hashbrown::{HashMap, HashSet};

#[derive(Serialize, Deserialize, Clone)]
pub struct NGramTrie {
    pub root: Box<TrieNode>,
    pub n_gram_max_length: u32,
    pub rule_set: Vec<String>
}

impl NGramTrie {
    pub fn new(n_gram_max_length: u32, root_capacity: Option<usize>) -> Self {
        let _rule_set = NGramTrie::_calculate_ruleset(n_gram_max_length - 1);
        NGramTrie {
            root: Box::new(TrieNode::new(root_capacity)),
            n_gram_max_length,
            rule_set: _rule_set
        }
    }

    //better to use this as it is simle, maybe even faster
    pub fn insert(&mut self, n_gram: &[u16]) {
        self.root.insert(n_gram);
    }

    pub fn merge(&mut self, other: &NGramTrie) {
        self.root.merge(&other.root);
    }

    pub fn size_in_ram(&self) -> usize {
        println!("----- Calculating size in RAM -----");
        let start = Instant::now();
        let size = mem::size_of::<NGramTrie>() + self.root.size_in_ram();
        let duration = start.elapsed();
        println!("Time taken to calculate size in RAM: {:?}", duration);
        println!("Size in RAM: {} MB", size as f64 / (1024.0 * 1024.0));
        size
    }

    pub fn shrink_to_fit(&mut self) {
        println!("----- Shrinking to fit -----");
        let start = Instant::now();
        self.root.shrink_to_fit();
        let duration = start.elapsed();
        println!("Time taken to shrink to fit: {:?}", duration);
    }

    pub fn save(&self, filename: &str) -> std::io::Result<()> {
        println!("----- Saving trie -----");
        let start = Instant::now();
        let file = File::create(filename)?;
        let writer = BufWriter::new(file);
        serialize_into(writer, self).map_err(|e| std::io::Error::new(std::io::ErrorKind::Other, e))?;
        let duration = start.elapsed();
        println!("Time taken to save trie: {:?}", duration);
        let file_size = metadata(filename).expect("Unable to get file metadata").len();
        let file_size_mb = file_size as f64 / (1024.0 * 1024.0);
        println!("Size of saved file: {:.2} MB", file_size_mb);
        Ok(())
    }

    pub fn load(filename: &str) -> std::io::Result<Self> {
        println!("----- Loading trie -----");
        let start = Instant::now();
        let file = File::open(filename)?;
        let reader = BufReader::new(file);
        let trie: NGramTrie = deserialize_from(reader).map_err(|e| std::io::Error::new(std::io::ErrorKind::InvalidData, e))?;
        let duration = start.elapsed();
        println!("Time taken to load trie: {:?}", duration);
        trie.size_in_ram();
        Ok(trie)
    }

    pub fn _preprocess_rule_context(tokens: &[u16], rule_context: Option<&str>) -> Vec<Option<u16>> {
        let mut result = Vec::new();
        if let Some(rule_context) = rule_context {
            assert!(tokens.len() >= rule_context.len(), "Tokens length must be at least as big as rule context length");
            let diff = tokens.len() - rule_context.len();
            for (&token, rule) in tokens[diff..].iter().zip(rule_context.chars()) {
                match rule {
                    '*' => result.push(None),
                    '-' => continue,
                    _ => result.push(Some(token)),
                }
            }
        } else {
            result = tokens.iter().map(|&t| Some(t)).collect();
        }
        result
    }

    pub fn _calculate_ruleset(n_gram_max_length: u32) -> Vec<String> {
        if n_gram_max_length == 1 {
            return vec!["+".to_string(), "-".to_string()];
        }
        let mut ruleset = Vec::<String>::new();
        ruleset.extend(NGramTrie::_calculate_ruleset(n_gram_max_length - 1));
    
        let characters = vec!["+", "*", "-"];
        
        let mut combinations : Vec<String> = (2..n_gram_max_length).fold(
            characters.iter().map(|c| characters.iter().map(move |&d| d.to_owned() + *c)).flatten().collect(),
            |acc,_| acc.into_iter().map(|c| characters.iter().map(move |&d| d.to_owned() + &*c)).flatten().collect()
        );
    
        combinations.retain(|comb| comb.starts_with('+'));
    
        let mut tokens = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".to_string();
        tokens.truncate(n_gram_max_length as usize);
        let mut hashmap = HashMap::<String, String>::new();
    
        for comb in combinations {
            let mut key = "".to_string();
            for (token, rule) in tokens.chars().zip(comb.chars()) {
                match rule {
                    '*' => key += "*",
                    '-' => continue,
                    _ => key += &token.to_string(),
                }
            }
            hashmap.insert(key, comb);
        }
    
        ruleset.extend(hashmap.values().cloned());
    
        ruleset
    }

    pub fn set_rule_set(&mut self, rule_set: Vec<String>) {
        println!("----- Setting rule set -----");
        self.rule_set = rule_set;
        println!("Rule set: {:?}", self.rule_set);
    }

    pub fn get_count(&self, rule: &[Option<u16>]) -> u32 {
        self.root.get_count(rule)
    }

    //TODO: merge with unique_continuation_count?
    pub fn find_all_nodes(&self, rule: &[Option<u16>]) -> Vec<&TrieNode> {
        self.root.find_all_nodes(rule)
    }

    pub fn unique_continuations(&self, rule: &[Option<u16>]) -> HashSet<u16> {
        let mut unique = HashSet::<u16>::new();
        for node in self.find_all_nodes(rule) {
            unique.extend(node.children.keys());
        }
        unique
    }

    //TODO: Cache??
    pub fn probability_for_token(&self, smoothing: &impl Smoothing, history: &[u16], predict: u16) -> Vec<(String, f64)> {
        let mut rules_smoothed = Vec::<(String, f64)>::new();

        for r_set in &self.rule_set.iter().filter(|r| r.len() <= history.len()).collect::<Vec<_>>()[..] {
            let mut rule = NGramTrie::_preprocess_rule_context(history, Some(&r_set));
            rule.push(Some(predict));
            rules_smoothed.push((r_set.to_string(), smoothing.smoothing(&self, &rule)));
        }

        rules_smoothed
    }

    pub fn get_prediction_probabilities(&self, smoothing: &impl Smoothing, history: &[u16]) -> Vec<(u16, Vec<(String, f64)>)> { 
        println!("----- Getting prediction probabilities -----");
        let start = Instant::now();
        let mut prediction_probabilities = Vec::<(u16, Vec<(String, f64)>)>::new();

        for token in self.root.children.keys() {
            let probabilities = self.probability_for_token(smoothing, history, *token);
            prediction_probabilities.push((*token, probabilities));
        }

        let duration = start.elapsed();
        println!("Time taken to get prediction probabilities: {:?}", duration);

        prediction_probabilities
    }

    pub fn estimate_time_and_ram(tokens_size: usize) -> (f64, f64) {
        let x = tokens_size as f64;
        let y = 0.0021 * x.powf(0.8525);
        let _x = (y / 0.0021).powf(1.0 / 0.8525) as f64; //how many can be fit in RAM
        let t = (2.8072 * x / 1_000_000.0 - 0.124) / 60.0; //how long it will take to fit
        println!("Expected time for {} tokens: {} min", tokens_size, t);
        println!("Expected ram usage for {} tokens: {} MB", tokens_size, y);
        (t, y)
    }
    
    pub fn fit(tokens: Arc<Vec<u16>>, n_gram_max_length: u32, root_capacity: Option<usize>, max_tokens: Option<usize>) -> Self {
        println!("----- Trie fitting -----");
        let tokens_size = max_tokens.unwrap_or(tokens.len());
        NGramTrie::estimate_time_and_ram(tokens_size);
        let mut trie = NGramTrie::new(n_gram_max_length, root_capacity);
        let max_tokens = max_tokens.unwrap_or(tokens.len()).min(tokens.len());
        let start = Instant::now();
        for i in tqdm(0..max_tokens - n_gram_max_length as usize + 1) {
            trie.insert(&tokens[i..i + n_gram_max_length as usize]);
        }
        let duration = start.elapsed();
        println!("Time taken to fit trie: {:?}", duration);
        trie.shrink_to_fit();
        trie.size_in_ram();
        trie
    }

    #[deprecated]
    pub fn fit_multithreaded(tokens: Arc<Vec<u16>>, ranges: Vec<Range<usize>>, n_gram_max_length: u32, root_capacity: Option<usize>) -> Self {
        let mut trie = NGramTrie::new(n_gram_max_length, root_capacity);

        let mut handles = vec![];

        for range in ranges {
            let mut trie_clone = trie.clone();

            let _tokens = tokens.clone();

            let handle = std::thread::spawn(move || {
                for i in range.start..range.end - n_gram_max_length as usize + 1 {
                    let n_gram = &_tokens[i..i + n_gram_max_length as usize];
                    trie_clone.insert(n_gram);
                }
                trie_clone
            });

            handles.push(handle);
        }

        for handle in handles {
            let partial_trie = handle.join().unwrap();
            trie.merge(&partial_trie);
        }
        trie
    }

    #[deprecated]
    pub fn fit_multithreaded_recursively(tokens: Arc<Vec<u16>>, ranges: Vec<Range<usize>>, n_gram_max_length: u32, root_capacity: Option<usize>) -> Self {
        if ranges.len() > 1 {
            let mid = ranges.len() / 2;
            let left = ranges[..mid].to_vec();
            let right = ranges[mid..].to_vec();
            // Recursively process both halves
            let right_clone = tokens.clone();
            let handle = std::thread::spawn(move || {
                NGramTrie::fit_multithreaded_recursively(right_clone, right, n_gram_max_length, root_capacity)
            });
            let mut left_trie = NGramTrie::fit_multithreaded_recursively(tokens, left, n_gram_max_length, root_capacity);
            let right_trie = handle.join().unwrap();
            left_trie.merge(&right_trie);
            left_trie
        } else {
            let mut trie = NGramTrie::new(n_gram_max_length, root_capacity);
            let range = &ranges[0];
            for i in range.start..range.end - n_gram_max_length as usize + 1 {
                let n_gram = &tokens[i..i + n_gram_max_length as usize];
                trie.insert(n_gram);
            }
            trie
        }
    }

    pub fn load_json(filename: &str, max_tokens: Option<usize>) -> std::io::Result<Arc<Vec<u16>>> {
        println!("----- Loading tokens -----");
        let file = File::open(filename)?;
        let reader = BufReader::new(file);
        let start = std::time::Instant::now();
        let mut tokens: Vec<u16> = serde_json::from_reader(reader).map_err(|e| std::io::Error::new(std::io::ErrorKind::InvalidData, e))?;
        let duration = start.elapsed();
        println!("Time taken to load tokens: {:?}", duration);
        println!("Size of tokens in RAM: {:.2} MB", (tokens.len() * std::mem::size_of::<u16>()) as f64 / 1024.0 / 1024.0);
        if let Some(max) = max_tokens {
            if max < tokens.len() {
                tokens.truncate(max);
            }
        }
        println!("Size of tokens in RAM after truncation: {:.2} MB", (tokens.len() * std::mem::size_of::<u16>()) as f64 / 1024.0 / 1024.0);
        println!("Tokens loaded: {}", tokens.len());
        Ok(Arc::new(tokens))
    }
    
    #[deprecated]
    pub fn split_into_ranges(tokens: Arc<Vec<u16>>, max_tokens: usize, number_of_chunks: usize, n_gram_max_length: u32) -> Vec<Range<usize>> {
        let mut ranges = Vec::new();
        let max_tokens = std::cmp::min(max_tokens, tokens.len());
        let chunk_size = (max_tokens as f64 / number_of_chunks as f64).ceil() as usize;
        for i in 0..number_of_chunks {
            let start = i * chunk_size;
            let end = if i == number_of_chunks - 1 {
                max_tokens
            } else {
                (i + 1) * chunk_size + n_gram_max_length as usize - 1
            };
            ranges.push(start..end);
        }
        ranges
    }

}