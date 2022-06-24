#[allow(unused)]
use std::collections::HashMap;

/// Task-10
/// not correct!!!
fn is_match(s: String, p: String) -> bool {
    let ss = s.as_str();
    let ps = p.as_str();
    if ps.len() == 0 { return ss.len() == 0 }
    let pf = &ps[..1];
    if pf != "*" {
        if pf != "." && pf != &ss[..1] { return false }
        return is_match(ss[1..].to_string(), ps[1..].to_string())
    } else {
        for i in 0..=ss.len() {
            if is_match(ss[i..].to_string(), ps[1..].to_string()) {
                return true
            }
        }
    }
    false
}

/// Task-8
/// Implement the myAtoi(string s) function, which converts a string
/// to a 32-bit signed integer (similar to C/C++'s atoi function).
pub fn my_atoi(s: String) -> i32 {
    let xs = s.as_str().trim_start();
    if xs.len() == 0 { return 0 }
    let (mut pluses, mut minuses) = (1u8, 0u8);
    let mut digits: Vec<u8> = vec![];
    // input string parsing
    for (i, x) in xs.chars().enumerate() {
        if i == 0 {
            match x {
                '-' => (pluses, minuses) = (0, 1),
                '+' => continue,
                '0'..='9' => digits.push(x as u8 - '0' as u8),
                _ => return 0
            }
            continue
        }
        match x {
            '0'..='9' => digits.push(x as u8 - '0' as u8),
            _ => break
        }
    }
    // sign
    let sign = pluses as i8 - minuses as i8;
    // number
    let ls = digits.len();
    // нет цифр
    if ls == 0 { return 0 }
    // находим первую значащую цифру, пропуская лидирующие нули
    let mut k = 0;
    while k < ls && digits[k] == 0 { k += 1 }
    // если все цифры нули, то возвращаем 0
    if k > 0 && k == ls { return 0 }
    // если количество разрядов превышает допустимое для i32, возвращаем лимиты
    if ls - k > 10 { return if sign < 0 { i32::MIN } else { i32::MAX } }
    // считаем число
    let mut s = 0u64;
    let mut p = 1u64;
    for i in (k..ls).rev() {
        s += p * digits[i] as u64;
        p *= 10;
    }
    if sign >= 0 && s > i32::MAX as u64 { return i32::MAX }
    if sign < 0 && s > (1 << 31) { return i32::MIN }
    if sign < 0 { -(s as i32) } else { s as i32 }
}

/// Преобразование натурального числа в римскую нотацию
pub fn int_to_roman(n: u32) -> String {
    let keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000];
    let vals = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"];
    let mut size = keys.len();
    // проверяем входное значение на наличие в keys
    if keys.contains(&n) {
        for i in 0..size {
            if keys[i] == n { return vals[i].to_string() }
        }
    }
    // формируем ответ
    let mut m = n;
    let mut r = "".to_string();
    size -= 1;
    for i in 0..=size {
        let x = m / keys[size - i];
        if x == 0 { continue }
        m -= x * keys[size - i];
        for _ in 0..x { r += vals[size - i] }
        if m == 0 { break }
    }
    r
}

/// Вычисление степени
// Условие расчета: n > 0
fn pow(x: f64, n: i32) -> f64 {
    if n == 1 { return x }
    let p = pow(x * x, n / 2);
    return if n & 1 == 0 { p } else { x * p }
}

// General type T wrapper's declaration
struct F<T> { f: T }

// Реализация обертки для конкретного типа - функции Fn(f64, i32) -> f64
impl<T> F<T> where T: Fn(f64, i32) -> f64 {
    fn new(f: T) -> Self { Self { f } }
    fn f(&self, arg1: f64, arg2: i32) -> f64 {
        // проверяем на граничные значения
        if arg2 > i32::MIN {
            (self.f)(arg1, arg2.abs())
        } else {
            arg1 * (self.f)(arg1, i32::MAX)
        }
    }
}

pub fn my_pow(x: f64, n: i32) -> f64 {
    let zero = 0f64;
    let one = 1f64;
    // замыкание - обратное значение
    let inv = |x: f64, n: i32| if n < 0 { one / x } else { x };
    // проверяем особые случаи
    if n == 0 { return one }
    if n == 1 || x == zero || x == one { return x }
    if n == -1 { return inv(x, n) }
    if x == -one && n == i32::MIN { return one }
    // расчет
    F::new(pow).f(inv(x, n), n)
}

/// Задача с leetcode
pub fn longest_palindrome(s: String) -> String {
    let is_palindrome = |x: &str| {
        let l = x.len();
        for i in 0..(l / 2) {
            if &x[i..(i + 1)] != &x[(l - i - 1)..(l - i)] { return false }
        }
        return true
    };
    let length = s.len();
    let r = s.as_str();
    if length == 1 || is_palindrome(r) { return s }
    if length == 2 {
        return if &r[..1] == &r[1..] { s } else { (&r[..1]).to_string() }
    }
    let mut v = "".to_string();
    let mut max_length = 0;
    for i in 0..(length - 1) {
        for j in (i + 1)..length {
            if j - i > max_length {
                let x = &r[i..=j];
                if is_palindrome(x) {
                    max_length = j - i;
                    v = x.to_string();
                }
            }
        }
    }
    if v.len() == 0 { (&r[..1]).to_string() } else { v }
}

// x * m
pub fn mul(x: u64, m: u64) -> u64 {
    if m == 1 { return x }
    let y = mul(x << 1, m >> 1);
    if m & 1 == 0 { y } else { x + y }
}

/// Task-29
/// Given two integers dividend and divisor, divide two integers
/// without using multiplication, division, and mod operator.
/// Return the quotient after dividing dividend by divisor
/// If the quotient is strictly greater than 2³¹ - 1, then return 2³¹ - 1,
/// and if the quotient is strictly less than -2³¹, then return -2³¹
pub fn divide(dividend: i32, divisor: i32) -> i32 {
    if divisor == 1 { return dividend }
    if divisor == -1 { return if dividend == i32::MIN { i32::MAX } else { -dividend } }
    if dividend == divisor { return 1 }
    if dividend == 0 { return 0 }
    let sgn = |x| if x > 0 { 1 } else { -1 };
    let sign = sgn(dividend) * sgn(divisor);
    let mut a = (dividend as i64).abs() as u64;
    let b = (divisor as i64).abs() as u64;
    // проверяем границы quotient
    let x = if sign > 0 { i32::MAX as u64 } else { 1 << 31 };
    let mut y = mul(x, b);
    if a >= y { return if sign > 0 { i32::MAX } else { i32::MIN } }
    // quotient внутри интервала i32, можно не опасаться overflow
    // если числитель большой, а знаменатель маленький, считать просто вычитанием будет очень долго
    let mut q = 0i32;
    while a >= b { a -= b; q += 1 }
    if sign > 0 { q } else { -q }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn int_to_roman_tests() {
        assert_eq!("III", int_to_roman(3));
        assert_eq!("IV", int_to_roman(4));
        assert_eq!("IX", int_to_roman(9));
        assert_eq!("LVIII", int_to_roman(58));
        assert_eq!("MCMXCIV", int_to_roman(1994));
    }

    #[test]
    fn is_match_tests() {
        assert_eq!(is_match("aa".to_string(), "a".to_string()), false);
        assert_eq!(is_match("aa".to_string(), "a*".to_string()), true);
        assert_eq!(is_match("ab".to_string(), ".*".to_string()), true);
    }

    #[test]
    fn my_atoi_test() {
        assert_eq!(my_atoi("4193 with words".to_string()), 4193);
        assert_eq!(my_atoi("   -42".to_string()), -42);
        assert_eq!(my_atoi("3.14152".to_string()), 3);
        assert_eq!(my_atoi("00000-42a1234".to_string()), 0);
        assert_eq!(my_atoi("    0000000000000   ".to_string()), 0);
        assert_eq!(my_atoi("-000000000000001".to_string()), -1);
        assert_eq!(my_atoi("-2147483649".to_string()), i32::MIN);
        assert_eq!(my_atoi("123-".to_string()), 123);
    }

    #[test]
    fn divide_test() {
        assert_eq!(divide(10, 3), 3);
        assert_eq!(divide(7, -3), -2);
        assert_eq!(divide(-2147483648, 2), -1073741824);
    }

    #[test]
    fn pow_tests() {
        assert_eq!(my_pow(2_f64, 10), 1024f64);
        assert_eq!(my_pow(2.1f64, 3), 9.261000000000001);
        assert_eq!(my_pow(-1f64, i32::MIN), 1f64);
        assert_eq!(my_pow(-2f64, i32::MIN), 0f64);
    }
}
