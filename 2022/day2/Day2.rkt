#lang racket

(define in
  (open-input-file "/Users/jacobkline/Documents/Coding/Advent-Of-Code/2022/day2/input.txt"))

(define string-input (read-string 20000 in))
(define loi (string-split string-input "\n"))

;; To calculate the score of the given individual game of RPS
;; LOS -> Number
(define (calc-score tuple)
  (local [
          (define outcome-score (cond
                      [(or (and (equal? (first tuple) "A") (equal? (second tuple) "X"))
                           (and (equal? (first tuple) "B") (equal? (second tuple) "Y"))
                           (and (equal? (first tuple) "C") (equal? (second tuple) "Z"))) 3]
                      [(or (and (equal? (first tuple) "A") (equal? (second tuple) "Z"))
                           (and (equal? (first tuple) "B") (equal? (second tuple) "X"))
                           (and (equal? (first tuple) "C") (equal? (second tuple) "Y"))) 0]
                      [else 6]))
          (define choice-score (cond
                          [(equal? (second tuple) "X") 1]
                          [(equal? (second tuple) "Y") 2]
                          [else 3]))
          ]
          (+ outcome-score choice-score)))

;; To calculate the score of an entire list of games of RPS
;; LOS -> Number
(define (get-score input cur-score)
  (local [
          (define cur-round-score (calc-score (string-split (first input) " ")))
          (define new-input (rest input))
          ]
    (cond
      [(> (length new-input) 0) (get-score new-input (+ cur-score cur-round-score))]
      [else (+ cur-score cur-round-score)])))

(println (get-score loi 0))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;             Part 2               ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; To calculate the score of the given individual game of RPS
;; LOS -> Number
(define (calc-score2 tuple)
  (local [(define outcome-score (cond
                      [(equal? (second tuple) "X") 0]
                      [(equal? (second tuple) "Y") 3]
                      [(equal? (second tuple) "Z") 6]))
          (define choice-score (cond
                          [(or (and (= outcome-score 6) (equal? (first tuple) "A"))
                               (and (= outcome-score 3) (equal? (first tuple) "B"))
                               (and (= outcome-score 0) (equal? (first tuple) "C"))) 2]
                          [(or (and (= outcome-score 6) (equal? (first tuple) "B"))
                               (and (= outcome-score 0) (equal? (first tuple) "A"))
                               (and (= outcome-score 3) (equal? (first tuple) "C")))3]
                          [(or (and (= outcome-score 6) (equal? (first tuple) "C"))
                               (and (= outcome-score 3) (equal? (first tuple) "A"))
                               (and (= outcome-score 0) (equal? (first tuple) "B"))) 1]))]
          (+ outcome-score choice-score)))

;; To calculate the score of an entire list of games of RPS
;; LOS -> Number
(define (get-score2 input cur-score)
  (local [(define cur-round-score (calc-score2 (string-split (first input) " ")))
          (define new-input (rest input))]
    (cond
      [(> (length new-input) 0) (get-score2 new-input (+ cur-score cur-round-score))]
      [else (+ cur-score cur-round-score)])))

(println (get-score2 loi 0))