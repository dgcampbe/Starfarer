//standard library
use std::string::String;
use std::hash::{Hash, Hasher};
//external crates
//cryptography
extern crate merkle;
extern crate ring;
//rand
extern crate rand;
use rand::{Rng, RngCore};
use rand::os::{OsRng};
//time
extern crate time;
//chrono
extern crate chrono;
//error-chain
extern crate error_chain;
//rayon
extern crate rayon;
//cpython -will be enabled later
//#[macro_use]
//extern crate cpython;
//use cpython::{Python, PyResult};

struct Blockchain {

    name: String,
    genesis_block: Block<>

}

struct Block {

    size: u32,
    previous_hash: u32,
    vote: u32,
    version: u32,
    difficulty: u128,
    timestamp: i128,
    nonce: u128,
}

struct Transaction {

    tokens: Vec<u32>, //(Token)
    locking_script: String,
    payload: i64,
}

impl std::fmt::Display for Transaction {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "(tokens: {:?}, locking_script: {}, payload: {})", self.tokens, self.locking_script, self.payload)
    }
}
fn main() {
    let test_transaction = Transaction {
        tokens: [123].to_vec(),
        locking_script: "abc".to_string(),
        payload: 456
    };

    let test_block = Block {
        size: 1,
        previous_hash: 2,
        vote: 3,
        version: 4,
        difficulty: 5,
        timestamp: 6,
        nonce: 7,
    };

    let test_blockchain = Blockchain {
        name: "test".to_string(),
        genesis_block: test_block
    };

    println!("{}", test_transaction);
    rand_test();
}


fn rand_test() {

    let mut r = OsRng::new().unwrap();
    let mut my_secure_bytes = vec![0u8; 1500];
    r.fill_bytes(&mut my_secure_bytes);
    let my_secure_int: u64 = r.gen();

    println!("First few bytes = {:?}; random int = {:?}",
        &my_secure_bytes[..5], my_secure_int);
}
//py_module_initializer!(tp2p, ) //needs work
