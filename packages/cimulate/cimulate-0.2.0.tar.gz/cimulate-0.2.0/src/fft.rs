use std::f64::consts::PI;

use num_complex::Complex;

const I: Complex<f64> = Complex { re: 0.0, im: 1.0 };

pub fn fft(input: &[Complex<f64>]) -> Vec<Complex<f64>> {
    fn fft_inner(buf_a: &mut [Complex<f64>], buf_b: &mut [Complex<f64>], n: usize, step: usize) {
        if step >= n {
            return;
        }

        fft_inner(buf_b, buf_a, n, step * 2);
        fft_inner(&mut buf_b[step..], &mut buf_a[step..], n, step * 2);
        let (left, right) = buf_a.split_at_mut(n / 2);

        for i in (0..n).step_by(step * 2) {
            let t = (-I * PI * (i as f64) / (n as f64)).exp() * buf_b[i + step];
            left[i / 2] = buf_b[i] + t;
            right[i / 2] = buf_b[i] - t;
        }
    }

    let n_orig = input.len();
    let n = n_orig.next_power_of_two();

    let mut buf_a = input.to_vec();
    buf_a.append(&mut vec![Complex { re: 0.0, im: 0.0 }; n - n_orig]);

    let mut buf_b = buf_a.clone();
    fft_inner(&mut buf_a, &mut buf_b, n, 1);
    buf_a
}

pub fn ifft(input: &mut [Complex<f64>]) {
    let n = input.len();

    // Conjugate the input, perform FFT, then conjugate again and divide by n.
    for x in input.iter_mut() {
        *x = x.conj();
    }

    fft(input);

    for x in input.iter_mut() {
        *x = x.conj() / n as f64;
    }
}

pub fn fftfreq(n: usize, d: f64) -> Vec<f64> {
    let mut freqs = Vec::with_capacity(n);
    let inv_n = 1.0 / (n as f64 * d);
    let n_half = n / 2;

    for i in 0..n_half {
        freqs.push(i as f64 * inv_n);
    }

    for i in n_half..n {
        freqs.push((i as f64 - n as f64) * inv_n);
    }

    freqs
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fft() {
        let mut input = vec![
            Complex::new(1.0, 0.0),
            Complex::new(2.0, 0.0),
            Complex::new(3.0, 0.0),
            Complex::new(4.0, 0.0),
        ];

        fft(&mut input);

        let expected = vec![
            Complex::new(10.0, 0.0),
            Complex::new(-2.0, 2.0),
            Complex::new(-2.0, 0.0),
            Complex::new(-2.0, -2.0),
        ];

        for (computed, &expected) in input.iter().zip(&expected) {
            assert!((computed.re - expected.re).abs() < 1e-10);
            assert!((computed.im - expected.im).abs() < 1e-10);
        }
    }

    #[test]
    fn test_ifft() {
        // Test FFT and IFFT correctness
        let mut data = vec![
            Complex::new(1.0, 0.0),
            Complex::new(1.0, 0.0),
            Complex::new(0.0, 0.0),
            Complex::new(0.0, 0.0),
        ];

        // Perform FFT
        fft(&mut data);

        // Perform IFFT
        ifft(&mut data);

        // Compare original input with the result of IFFT
        let original_data = vec![
            Complex::new(1.0, 0.0),
            Complex::new(1.0, 0.0),
            Complex::new(0.0, 0.0),
            Complex::new(0.0, 0.0),
        ];

        for (orig, ifft_val) in original_data.iter().zip(data.iter()) {
            assert!((orig.re - ifft_val.re).abs() < 1e-10);
            assert!((orig.im - ifft_val.im).abs() < 1e-10);
        }
    }

    #[test]
    fn test_fftfreq() {
        // Test fftfreq function with sample spacing 1.0
        let n = 8;
        let freqs = fftfreq(n, 1.0);
        let expected_freqs = vec![0.0, 0.125, 0.25, 0.375, -0.5, -0.375, -0.25, -0.125];

        for (f, ef) in freqs.iter().zip(expected_freqs.iter()) {
            assert_eq!(f, ef);
        }

        // Test fftfreq with a different sample spacing
        let n = 8;
        let d = 0.5;
        let freqs = fftfreq(n, d);
        let expected_freqs = vec![0.0, 0.25, 0.5, 0.75, -1.0, -0.75, -0.5, -0.25];

        for (f, ef) in freqs.iter().zip(expected_freqs.iter()) {
            assert_eq!(f, ef);
        }
    }
}
