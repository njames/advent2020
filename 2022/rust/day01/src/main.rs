pub fn main() {
    println!(
        "Answer: {}",
        include_str!("../../../input/day01/input01.txt")
            .split("\n\n")
            .map(|e| e.lines().map(|c| c.parse::<u32>().unwrap()).sum::<u32>())
            .max()
            .unwrap(),
    );
}