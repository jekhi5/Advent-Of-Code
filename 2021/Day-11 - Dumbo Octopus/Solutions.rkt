;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname Solutions) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define-struct pairing [level flashed? num-flashes])
; An OctopusLevelReading is a (make-pairing OctopusNumber Boolean)
; A (make-octopus l f) represents an octopus with an energy level, l
; and a status of whether or not it flashed this step, f

(define pair-1 (make-pairing 5 #false 0))
(define pair-2 (make-pairing 0 #true 34))
(define pair-3 (make-pairing 9 #true 2))

; pairing-temp : Pairing -> ?
(define (pairing-temp p-t)
  (... (pairing-level p-t) ... (pairing-flashed? p-t) ... (pairing-num-flashes p-t) ...))

; An {X} [Grid-of X] is a [List-of [List-of X]] where all rows are of an equal length

(define grid-1 '((1  2  3  4  5)
                 (6  7  8  9  10)
                 (11 12 13 14 15)))
(define grid-2 '((a b c d e)
                 (f g h i j)))
(define grid-3 '(("hi" "there")))

; An OctopusNumber is one of:
; - 0
; - 1
; - 2
; - 3
; - 4
; - 5
; - 6
; - 7
; - 8
; - 9
; And represents an octopuses level

(define octonum-0 0)
(define octonum-0 1)
(define octonum-0 2)
(define octonum-0 3)
(define octonum-0 4)
(define octonum-0 5)
(define octonum-0 6)
(define octonum-0 7)
(define octonum-0 8)
(define octonum-0 9)

; octopusnumber-temp : OctopusNumber -> ?
(define (octopusnumber-temp on-t)
  (cond [(= on-t 0) ...]
        [(= on-t 1) ...]
        [(= on-t 2) ...]
        [(= on-t 3) ...]
        [(= on-t 4) ...]
        [(= on-t 5) ...]
        [(= on-t 6) ...]
        [(= on-t 7) ...]
        [(= on-t 8) ...]
        [(= on-t 9) ...]))

; take-step : [Grid-of OctapusLevelReading] -> [Grid-of OctapusLevelReading]
; returns the resulting grid after one step is taken

(check-expect (take-step '((11111)
                           (19991)
                           (19191)
                           (19991)
                           (11111)))
              '((45654)
                (51115)
                (61116)
                (51115)
                (45654)))

; update-flashes : [Grid-of OctapusLevelReading] -> [Grid-of PctapusLevelReading]
; returns the grid after all neighboring flashes have been updated
(define (update-flashes grid)
  (local [(define updated-grid (map (λ(row) (map (λ(val) (make-pairing (add1 (pairing-level val)) row)) grid))


                                (cond [(andmap (λ(row) (map (λ(val) (< 10 (pairing-level val))) row) grid)) grid]
        [else 

(define (take-step grid)
  (local [(define initial-change (map (λ(row)
                                        (map (λ(val)
                                               (make-pairing (add1 (pairing-level val))
                                                             #true
                                                             (if (> 9 (pairing-level val))
                                                                 (add1 (pairing-flashes val))
                                                                 (pairing-flashes val)))) row)
                                        grid)))]
    (update-flashes initial-change)))

; take-n-steps : [Grid-of OctopusLevelReading] Number -> Number
; Returns the number of flashes after n steps are taken

(define (take-n-steps grid n)
  (cond [(zero? n)
         (local [(define grid-of-scores (map (λ(row) (map pairing-flashes row)) grid))
                 (define lo-scores (map (λ(row) (apply + row)) grid-of-scores))]
           (apply + lo-scores))]
        [(positive? n) (local [(define updated-grid (take-step grid))]
                         (take-n-steps updated-grid (sub1 n)))]))
