;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname Solutions) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/batch-io)
(define loud-input (read-lines "Input-File.rkt"))
(define input-string (filter (λ(strng) (and (not (string=? (substring strng 0 1) ";"))
                                            (not (string=? (substring strng 0 1) "#")))) loud-input))
(define input-lo-individual-string (map explode input-string))
(define input (map (λ(lolos) (map string->number lolos)) input-lo-individual-string))

; get-row-col : {X} [List-of [List-of X]] Number Number -> X
; returns the index at the given row and col.  If either is out of boudns, error

(define graph-1 (list '(1  2  3  4  5)
                      '(6  7  8  9  10)
                      '(11 12 13 14 15)))
(define graph-2 (list '(a b c d e)
                      '(f g h i j)
                      '(k l m n o)
                      '(p q r s t)
                      '(u v w x y)))

(check-expect (get-row-col graph-1 2 2) 13)
(check-expect (get-row-col graph-1 0 0) 1)
(check-expect (get-row-col graph-1 2 4) 15)
(check-error (get-row-col graph-1 3 4))
(check-error (get-row-col graph-1 1 5))

(check-expect (get-row-col graph-2 2 2) 'm)
(check-expect (get-row-col graph-2 0 0) 'a)
(check-expect (get-row-col graph-2 2 4) 'o)
(check-expect (get-row-col graph-2 3 4) 't)
(check-error (get-row-col graph-2 1 5))

(check-error (get-row-col '() 1 1))

(define (get-row-col 2d-array row col)
  (if (or (empty? 2d-array)
          (not (list? (first 2d-array))))
      (error 2d-array " is not a valid 2d-array")
      (local [(define given-row
                (if (< row (length 2d-array))
                    (list-ref 2d-array row)
                    (error "Index " row " out of bounds in given 2d-array: " 2d-array)))
              (define given-val
                (if (< col (length given-row))
                    (list-ref given-row col)
                    (error "Index " col " out of bounds in given row: " given-row)))]
        given-val)))


; get-minimum-values : [List-of [List-of Number]] -> [List-of Number]
; returns a list of the lowpoints in the graph
; ASSUME: All lengths of each sublist are equal

(define testing-input '((2 1 9 9 9 4 3 2 1 0)
                        (3 9 8 7 8 9 4 9 2 1)
                        (9 8 5 6 7 8 9 8 9 2)
                        (8 7 6 7 8 9 6 7 8 9)
                        (9 8 9 9 9 6 5 6 7 8)))

(check-expect (get-minimum-values testing-input) '(1 0 5 5))

(define (get-minimum-values graph)
  (if (empty? graph) '()
      (local [; get-minimum-values/acc : Number Number -> [List-of Number]
              ; Returns a list of the lowpoints in the graph
              ; ACCUMULATOR: _row_ represents the index of the current row being checked
              ; ACCUMULATOR: _col_ represents the index of the current column being checked
              (define (get-minimum-values/acc row col)
                (cond [(= row (length graph)) '()]
                      [(= col (length (first graph)))
                       (get-minimum-values/acc (add1 row) 0)]
                      [else
                       (local [(define cur-row (first graph))

                               (define cur-val (get-row-col graph row col))

                               (define below-val (if (= row (sub1 (length graph)))
                                                     (add1 cur-val)
                                                     (get-row-col graph (add1 row) col)))
                               (define above-val (if (= row 0)
                                                     (add1 cur-val)
                                                     (get-row-col graph (sub1 row) col)))
                               (define left-val (if (= col 0)
                                                    (add1 cur-val)
                                                    (get-row-col graph row (sub1 col))))
                               (define right-val (if (= col (sub1 (length cur-row)))
                                                     (add1 cur-val)
                                                     (get-row-col graph row (add1 col))))]
                         (cond [(and (< cur-val below-val)
                                     (< cur-val above-val)
                                     (< cur-val left-val)
                                     (< cur-val right-val))
                                (cons cur-val (get-minimum-values/acc row (add1 col)))]
                               [else (get-minimum-values/acc row (add1 col))]))]))]
        (get-minimum-values/acc 0 0))))

(define result (get-minimum-values input))
(define risk-levels (map add1 result))
(define total (apply + risk-levels))
(string-append "The sum of all risk levels is: " (number->string total))


#|

; get-basin-sizes : [List-of [List-of Number]] -> [List-of Number]
; Returns a list of all of the sizes of the basins in the graph
(define (get-basin-sizes graph)
  (if (empty? graph) '()
      (local [; calculate-basin : [List-of [List-of Number]] Number Number Number -> Number
              ; Returns the size of the basin with the lowpoint at the given row col
              ; ACCUMULATOR: Accumulates the number of valid basin-points
              (define (calculate-basin graph/helper row col total)
                (local [(define extending-left-basin


              ; get-basin-sizes/acc : Number Number -> [List-of Number]
              ; Returns a list of basin sizes in the graph
              ; ACCUMULATOR: _row_ represents the index of the current row being checked
              ; ACCUMULATOR: _col_ represents the index of the current column being checked
              (define (get-basin-sizes/acc row col)
                (cond [(= row (length graph)) '()]
                      [(= col (length (first graph)))
                       (get-basin-sizes/acc (add1 row) 0)]
                      [else
                       (local [(define cur-row (first graph))

                               (define cur-val (get-row-col graph row col))

                               (define below-val (if (= row (sub1 (length graph)))
                                                     (add1 cur-val)
                                                     (get-row-col graph (add1 row) col)))
                               (define above-val (if (= row 0)
                                                     (add1 cur-val)
                                                     (get-row-col graph (sub1 row) col)))
                               (define left-val (if (= col 0)
                                                    (add1 cur-val)
                                                    (get-row-col graph row (sub1 col))))
                               (define right-val (if (= col (sub1 (length cur-row)))
                                                     (add1 cur-val)
                                                     (get-row-col graph row (add1 col))))]
                         (cond [(and (< cur-val below-val)
                                     (< cur-val above-val)
                                     (< cur-val left-val)
                                     (< cur-val right-val))
                                (cons (calculate-basin graph row col 0)
                                      (get-basin-sizes/acc row (add1 col)))]
                               [else (get-basin-sizes/acc row (add1 col))]))]))]
        (get-basin-sizes/acc 0 0))))

|#