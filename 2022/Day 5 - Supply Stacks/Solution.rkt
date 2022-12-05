#lang racket

(define in
  (open-input-file "input.txt"))

(define string-input (read-string 20000 in))
(define loi (cond
              [(and (string? string-input)
                    (> (length string-input) 0)) (string-split string-input "\n")]
              [else '()]))

(define (split-lines delim los)
   (map (λ (x) (string-split x delim)) los))