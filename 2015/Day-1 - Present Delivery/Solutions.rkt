;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname Solutions) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(require 2htdp/batch-io)

(define loud-input (read-1strings "Input-File.rkt"))
(define input (filter (λ(val) (or (string=? val "(") (string=? val ")"))) loud-input))

; A Direction is one of:
; - "("
; - ")"
; and represents a direction where "(" means up and ")" means down

(define UP "(")
(define DOWN ")")

; direction-temp : Direction -> ?
#;(define (direction-temp d-t)
    (cond [(string=? d-t "(") ...]
          [(string=? d-t ")") ...]))


; get-final-floor : [List-of Direction] Boolean -> Number
; If _basement-check?_ is true, returns the index where Santa enters the basement, or the
; floor he ends on if he never enters the basement.  If _basement-check?_ is false, returns
; the final floor santa ends on regardless of if he enters the basement

(check-expect (evaluate-directions (list "(" "(" "(" ")" ")" "(") #false) 2)
(check-expect (evaluate-directions (list "(" "(" "(" ")" "(") #false) 3)
(check-expect (evaluate-directions (list "(") #false) 1)
(check-expect (evaluate-directions (list ")") #false) -1)
(check-expect (evaluate-directions (list) #false) 0)

(check-expect (evaluate-directions (list "(" "(" "(" ")" ")" ")" ")") #true) 7)
(check-expect (evaluate-directions (list "(" ")" "(" ")" ")") #true) 5)
(check-expect (evaluate-directions (list ")" "(" ")" ")" ")" ")") #true) 1)
(check-expect (evaluate-directions (list ")") #true) 1)
(check-expect (evaluate-directions (list "(") #true) -1)
(check-expect (evaluate-directions (list "(" "(" "(" ")" ")" ")") #true) -1)

(define (evaluate-directions lod basement-check?)
  (local [; get-basement-index [List-of Direction] Number Nat -> Number
          ; Returns the (index + 1) of the direction that tells santa to enter the basement.
          ; If Santa never enters the basement, returns -1
          ; ACCUMULATOR: _cur-floor_ represents the current floor santa is on at any given moment
          ; ACCUMULATOR: _index_ increases every time to represent the current index being checked
          (define (get-basement-index lod/helper cur-floor index)
            (if (negative? cur-floor) index
                (cond [(empty? lod/helper) -1]
                      [(cons? lod/helper)
                       (local [(define FIRST-LOD (first lod/helper))]
                         (get-basement-index (rest lod/helper)
                                             (if (string=? FIRST-LOD "(")
                                                 (add1 cur-floor)
                                                 (sub1 cur-floor))
                                             (add1 index)))])))

          ; get-final-floor [List-of Direction] -> Number
          ; Returns the floor santa ends on
          (define (get-final-floor lod/helper)
            (cond [(empty? lod/helper) 0]
                  [(cons? lod/helper)
                   (local [(define FIRST-LOD (first lod/helper))]
                     (cond [(string=? FIRST-LOD "(") (add1 (get-final-floor (rest lod/helper)))]
                           [(string=? FIRST-LOD ")") (sub1 (get-final-floor (rest lod/helper)))]))]))]
    
    (if basement-check? (get-basement-index lod 0 0) (get-final-floor lod))))

(define final-position (evaluate-directions input #false))
(define basement-entry (evaluate-directions input #true))

(string-append "Santa will end on: Floor " (number->string final-position))
(string-append "Santa will enter the basement at instruction #" (number->string basement-entry))