#[allow(unused)]

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

#[cfg(test)]
mod tests {
    use super::*;
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
}
