;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname Solutions) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(require racket/control)
(require 2htdp/batch-io)

(define loud-input (read-lines "Input-File.rkt"))
(define input (filter (λ(val) (and (not (string=? ";" (string-ith val 0)))
                                   (not (string=? "#" (string-ith val 0))))) loud-input))

; An OpeningValue is one of:
; - #\(
; - #\[
; - #\{
; - #\<
; and represents an opening to a statement in a SubmarineString

(define opening-val-1 #\))
(define opening-val-2 #\])
(define opening-val-3 #\})
(define opening-val-4 #\>)

; openingvalue-temp : OpeningValue -> ?
#;(define (openingvalue-temp ov-t)
  (cond [(char=? #\() ...]
        [(char=? #\[) ...]
        [(char=? #\{) ...]
        [(char=? #\<) ...]))

; A ClosingValue is one of;
; - #\)
; - #\]
; - #\}
; - #\>
; and represents a closing to a statement in a submarine string

(define closing-val-1 #\))
(define closing-val-2 #\])
(define closing-val-3 #\})
(define closing-val-4 #\>)

; closingvalue-temp : ClosingValue -> ?
#;(define (closingvalue-temp cv-t)
  (cond [(char=? #\)) ...]
        [(char=? #\]) ...]
        [(char=? #\}) ...]
        [(char=? #\>) ...]))

; A SubmarineString is a string containing only the following characters:
; - OpeningValue
; - ClosingValue
; A SubmarineString represents the output string from the Submarine's console

(define submarinestring1 "()")
(define submarinestring2 "[]")
(define submarinestring3 "{}")
(define submarinestring4 "<>")
(define submarinestring5 "{[}{{][][}{}{}{}]]()(<>][>)(<{}((")
(define submarinestring6 "{{{{{{{((((((<<<<>>>[[[[}[}[")

; submarinestring-temp : SubmarineString -> ?
#;(define (submarinestring-temp ss-t)
  (cond [(zero? (string-length ss-t)) ...]
        [(positive? (string-length ss-t)) ...]))

(define CLOSING-VALUES '(")" "}" "]" ">"))

; is-corrupted? : SubmarineString -> String
; Returns the first illegal character
; NOTE: This will return #false if the end of the string is reached and an opener is left 
;       without a match.  This is because the string is "incomplete" not "corrupted".
;       This function only finds corrupted strings

(check-expect (is-corrupted? "((()))") #false)
(check-expect (is-corrupted? "{{}{}}{}") #false)
(check-expect (is-corrupted? "<>") #false)
(check-expect (is-corrupted? "[[[][]][]]") #false)
(check-expect (is-corrupted? "()") #false)
(check-expect (is-corrupted? "") #false)
(check-expect (is-corrupted? "[[[[[[[[]]]") #false)

(check-expect (is-corrupted? "({)}") #true)
(check-expect (is-corrupted? "[][][]{}{{}<><>)()()") #true)
(check-expect (is-corrupted? "{}[]<>()[}") #true)
(check-expect (is-corrupted? "{([(<{}[<>[]}>{[]{[(<()>") #true)
(check-expect (is-corrupted? "[[<[([]))<([[{}[[()]]]") #true)
(check-expect (is-corrupted? "[{[{({}]{}}([{[{{{}}([]") #true)
(check-expect (is-corrupted? "[<(<(<(<{}))><([]([]()") #true)
(check-expect (is-corrupted? "<{([([[(<>()){}]>(<<{{") #true)


(define (is-corrupted? strng)
  (local [(define val-length (string-length strng))]
    (if (< val-length 2) #false
        (local [(define cur-val (substring strng 0 1))

                ; get-match : String -> String
                ; Returns the associated closing bracket match or #false if is closing value
                (define (get-match val)
                  (cond [(member? val CLOSING-VALUES) #false]
                        [(string=? val "(") ")"]
                        [(string=? val "{") "}"]
                        [(string=? val "[") "]"]
                        [(string=? val "<") ">"]))
                
                (define searching-val (get-match cur-val))

                ; is-corrupted?/acc : SubmarineString ClosingValue Number -> Boolean
                ; Does the given string have a matching closer?
                ; ACCUMULATOR: _searchin-value_ is set to the opening value's match each
                ;              time an open is found
                ; ACCUMULATOR: _number-of-enclosed_ represents the number of enclosed
                ;              completed matches
                (define (is-corrupted?/acc strng/helper searching-value number-of-enclosed)
                  (cond #;[(false? searching-value) #false] ; refers to a string starting with a 
                        ;                                     closing-value however, the problem
                        ;                                     prohibits this
                        [(= (string-length strng/helper) (string-length strng));inital acc run adjst.
                         (is-corrupted?/acc (substring strng/helper 1)
                                            searching-value
                                            number-of-enclosed)]
                        [(zero? (string-length strng/helper)) #false]
                        [(positive? (string-length strng/helper))
                         (local [(define first-val (substring strng/helper 0 1))]
                           (cond [(not (member? first-val CLOSING-VALUES))
                                  (or (is-corrupted?/acc (substring strng/helper 1)
                                                         (get-match first-val)
                                                         0)
                                      (is-corrupted?/acc (substring strng/helper 1)
                                                         searching-value
                                                         (add1 number-of-enclosed)))]
                                 [(member? first-val CLOSING-VALUES)
                                  (if (zero? number-of-enclosed)
                                      (not (string=? searching-value first-val))
                                      (is-corrupted?/acc (substring strng/helper 1)
                                                         searching-value
                                                         (sub1 number-of-enclosed)))]))]))
                                              

                (define result-is-corrupted? (if (false? searching-val)
                                                 #false
                                                 (is-corrupted?/acc strng searching-val 0)))]
          (if result-is-corrupted?
              #true
              (is-corrupted? (substring strng 1)))))))

; get-match : String -> String
; Returns the associated closing bracket match or #false if is closing value

(check-expect (get-match "(") ")")
(check-expect (get-match "[") "]")
(check-expect (get-match "{") "}")
(check-expect (get-match "<") ">")

(check-expect (get-match ")") "(")
(check-expect (get-match "]") "[")
(check-expect (get-match "}") "{")
(check-expect (get-match ">") "<")

(check-error (get-match "whattup"))

(define (get-match val)
  (cond [(string=? val "(") ")"]
        [(string=? val "[") "]"]
        [(string=? val "{") "}"]
        [(string=? val "<") ">"]
        [(string=? val ")") "("]
        [(string=? val "]") "["]
        [(string=? val "}") "{"]
        [(string=? val ">") "<"]
        [else (error "The given value : " val " is not a valid entry.")]))

; calculate-score : [List-of SubmarineString] -> Number
; Returns the score of the syntax errors

(check-expect (calculate-score '("[({(<(())[]>[[{[]{<()<>>"
                                 "[(()[<>])]({[<{<<[]>>("
                                 "{([(<{}[<>[]}>{[]{[(<()>"
                                 "(((({<>}<{<{<>}{[]{[]{}"
                                 "[[<[([]))<([[{}[[()]]]"
                                 "[{[{({}]{}}([{[{{{}}([]"
                                 "{<[[]]>}<{[{[{[]{()[[[]"
                                 "[<(<(<(<{}))><([]([]()"
                                 "<{([([[(<>()){}]>(<<{{"
                                 "<{([{{}}[<[[[<>{}]]]>[]]")) 26397)

(define (calculate-score los)
  (local [(define corrupted-strings (filter is-corrupted? los)
            #;(filter (λ(val) (member? (substring val (sub1 (string-length val))) CLOSING-VALUES))
                      los))

                
          ; get-illegal-char : String -> Char
          ; Returns the first illegal character in a string or false if no illegal chars
          (define (get-illegal-char strng searching-value number-of-enclosed)
            (cond #;[(zero? (string-length strng)) #false]
                  [(positive? (string-length strng))
                   (local [(define first-val (substring strng 0 1))]
                     (cond [(not (member? first-val CLOSING-VALUES))
                            (local [(define inner-result (get-illegal-char (substring strng 1)
                                                                           (get-match first-val)
                                                                           0))]

                              (cond [(char? inner-result) inner-result]
                                    [else (get-illegal-char (substring strng 1)
                                                            searching-value
                                                            (add1 number-of-enclosed))]))]
                           [(member? first-val CLOSING-VALUES)
                            (if (zero? number-of-enclosed)
                                (if (string=? searching-value first-val)
                                    #false
                                    (cond [(string=? first-val ")") #\)]
                                          [(string=? first-val "]") #\]]
                                          [(string=? first-val "}") #\}]
                                          [(string=? first-val ">") #\>]))
                                (get-illegal-char (substring strng 1)
                                                  searching-value
                                                  (sub1 number-of-enclosed)))]))]))

          (define lo-illegal-chars (map (λ(strng) (get-illegal-char (substring strng 1)
                                                                    (substring strng 0 1)
                                                                    0))
                                        corrupted-strings))
          (define lo-scores (map (λ(given-char)
                                   (cond [(char=? given-char #\)) 3]
                                         [(char=? given-char #\]) 57]
                                         [(char=? given-char #\}) 1197]
                                         [(char=? given-char #\>) 25137]
                                         #;[else 0]))
                                 lo-illegal-chars))]
    (apply + lo-scores)))

;(define corrupted-result (calculate-score input))
;(string-append "The total score of corrupted lines is: " (number->string corrupted-result))


; remove-final-pairing : SubmarineString -> String
; Removes the final pairing from the string and returns the resulting string

(check-expect (remove-final-pairing "[({(<(())[]>[[{[]{<()<>>") "[({(<(())[]>[[{[]{")
(check-expect (remove-final-pairing "{{}}") "")
(check-expect (remove-final-pairing "{{}[]}<({[(){}<><><>]})>") "{{}[]}")
(check-expect (remove-final-pairing "") "")

(define (remove-final-pairing strng)
  (if (zero? (string-length strng))
      ""
      (local [; remove-final-pairing/acc : SubmarineString ClosingValue Number -> String
              ; Removes the final pairing from the string and returns the resulting string
              ; ACCUMULATOR : Accumulaters the current search val, and how many levels deep it goes
              (define (remove-final-pairing/acc strng/helper search-val levels-deep)
                (local [(define given-length (string-length strng/helper))
                        (define last-char (string-ith strng/helper (sub1 given-length)))
                        (define resulting-substring (substring strng/helper 0 (sub1 given-length)))]

                  (if (member? last-char CLOSING-VALUES)
                      (remove-final-pairing/acc resulting-substring
                                                search-val (if (string=? last-char search-val)
                                                               (add1 levels-deep)
                                                               levels-deep))
                      (cond [(and (string=? last-char (get-match search-val)) (zero? levels-deep))
                             resulting-substring]
                            [(string=? last-char (get-match search-val))
                             (remove-final-pairing/acc resulting-substring
                                                       search-val
                                                       (sub1 levels-deep))]
                            [else (remove-final-pairing/acc resulting-substring
                                                            search-val
                                                            levels-deep)]))))]
        (remove-final-pairing/acc (substring strng 0 (sub1 (string-length strng)))
                                  (string-ith strng (sub1 (string-length strng)))
                                  0))))
           

; generate-extention : SubmarineString -> SubmarineString
; returns the required extension to the String in order to make it complete

(check-expect (generate-extension "(") ")")
(check-expect (generate-extension "[") "]")
(check-expect (generate-extension "{") "}")
(check-expect (generate-extension "<") ">")

(check-expect (generate-extension "[]{()<>}[()<{()}>{(") ")}]")
(check-expect (generate-extension "[({(<(())[]>[[{[]{<()<>>") "}}]])})]")
(check-expect (generate-extension "[(()[<>])]({[<{<<[]>>(") ")}>]})")
(check-expect (generate-extension "(((({<>}<{<{<>}{[]{[]{}") "}}>}>))))")
(check-expect (generate-extension "{<[[]]>}<{[{[{[]{()[[[]") "]]}}]}]}>")
(check-expect (generate-extension "<{([{{}}[<[[[<>{}]]]>[]]") "])}>")

(check-expect (generate-extension "") "")

(define (generate-extension strng)
  (if (zero? (string-length strng)) ""
      (local [; generate-extension/acc : SubmarineString ClosingValue -> String
              ; returns the required extension to the String in order to make it complete
              ; ACCUMULATOR: Accumulates the required extension
              (define (generate-extension/acc strng/helper extension)
                (cond [(zero? (string-length strng/helper)) extension]
                      [(positive? (string-length strng/helper))
                       (local [(define given-length (string-length strng/helper))
                               (define last-char (string-ith strng/helper (sub1 given-length)))]
                         (if (member? last-char CLOSING-VALUES)
                             (generate-extension/acc (remove-final-pairing strng/helper)
                                                      extension)
                             (generate-extension/acc (substring strng/helper 0 (sub1 given-length))
                                                     (string-append extension
                                                                    (get-match last-char)))))]))]
        (generate-extension/acc strng ""))))

; get-extension-score : SubmarineString -> Number
; Returns the score based on the extension

(check-expect (get-extension-score "])}>") 294)

(define (get-extension-score strng)
  (local [; get-extension-score/acc : SubmarineString Number -> Number
          ; Returns the score based on the extension
          ; ACCUMULATOR: Accumulates the current score
          (define (get-extension-score/acc strng/helper cur-score)
            (cond [(zero? (string-length strng/helper)) cur-score]
                  [(positive? (string-length strng/helper))
                   (local [(define first-val (string-ith strng/helper 0))

                           (define val->score (λ(val) (cond [(string=? val ")") 1]
                                                            [(string=? val "]") 2]
                                                            [(string=? val "}") 3]
                                                            [(string=? val ">") 4]
                                                            #;[else 0])))

                           (define first-score (val->score first-val))
                           (define new-score (+ (* cur-score 5) first-score))]
                     (get-extension-score/acc (substring strng/helper 1) new-score))]))]
    (get-extension-score/acc strng 0)))
                           


; get-median-score : [List-of SubmarineString] -> [List-of Number]
; Returns the median score based on a list of the submarines incomplete strings

(check-expect (get-median-score '("[({(<(())[]>[[{[]{<()<>>"
                                "[(()[<>])]({[<{<<[]>>("
                                "(((({<>}<{<{<>}{[]{[]{}"
                                "(((({<>}<{<{<>}{[]{[]{}"
                                "<{([{{}}[<[[[<>{}]]]>[]]")) 288957)

(define (get-median-score los)
  (local [(define incomplete-strings (filter (compose not is-corrupted?) los))

          (define lo-extensions (map generate-extension incomplete-strings))

          (define lo-scores (map get-extension-score lo-extensions))
          (define sorted-scores (sort lo-scores <))

          (define sorted-scores-length (length sorted-scores))]
    (list-ref sorted-scores (floor (/ sorted-scores-length 2)))))

;(define incomplete-result (get-median-score input))
;(string-append "The total score of incomplete lines is: " (number->string incomplete-result))