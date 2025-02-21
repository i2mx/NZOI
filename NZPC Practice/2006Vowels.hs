vowel 'a' = True
vowel 'e' = True
vowel 'i' = True
vowel 'o' = True
vowel 'u' = True
vowel 'A' = True
vowel 'E' = True
vowel 'I' = True
vowel 'O' = True
vowel 'U' = True
vowel _ = False

main = interact $ unlines . map (show . length . filter vowel) . takeWhile (/= "#") . lines