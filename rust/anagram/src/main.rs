use std::collections::HashMap;
use std::fs::File;
use std::io;
use std::io::BufRead;
use std::path::Path;


fn sorted_string(s: &str) -> String {
    let mut s = s.chars().collect::<Vec<_>>();
    s.sort();
    s.into_iter().collect::<String>()
}

struct Anagram(HashMap<String, Vec<String>>);

fn main() {
    println!("hello, world!")
    // 実行時にコマンドライン引数として単語を受け取る
    // let word = std::env::args().nth(1).expect("USAGE: word");
    // 辞書からAnagram構造体を作る
    // 多くのUnix環境では、このパスに辞書がある（ない場合は、手で辞書を準備してパスを変えてください）
    // let table = Anagram::new("/usr/share/dict/words").expect("failed to make table");

    // println!("{:?}", table.find(&word));
}
