# Regular Expression Workshop

線上測試/練習好網站
https://regex101.com/

[Workshop Slide](https://github.com/HannahLo/puzzle/blob/main/regex/Regular%20Expression%20Workshop.pdf)

[KQL](https://docs.microsoft.com/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference)

## Common

- 指定數量以上的字元
`{3,}` -> 三個以上
`{3,6}` -> 3 到 6 之間，左右包含

/a*b/ = /a{0,}b/
/a+b/ = /a{1,}b/
/a?b/ = /a{0,1}b/
/a?ab/ = /a{1,2}b/

- `?` 0 次或 1 次

- Caret Symbol `^`  (Start of line)
- Dollar Sign `$`   (End of line)

- `(?:...)`
A non-capturing group allows you to apply quantifiers to part of your regex but does not capture/assign an ID.

For example, repeating 1-3 digits and a period 3 times can be done like this: /(?:\d{1,3}\.){3}\d{1,3}/

- `[^abc]`
Matches any character except for an a, b or c
[] 裡有另外意義的指有 ^ 和 -, 其他都是字元本身
^ 不放在最前面代表自己本身
- 放在最前或最後代表自己本身


\W 不要字元 [^a-zA-z_]
\D 不要數字 [^0-9]



## Regex Flags

/a#comment here/**gmi** -> replace with flags, 可以同時使用

- **g**lobal
- **m**ulti line
- **i**sensitive
- e**x**tended
- **s**igle line

/(?i)test/ -> 在 regex 設定模式，開啟和 reset

開啟 insensitive
- (?i)

reset insensitive
- (?-i)
- (?^)


/(?i)test/
/te(?i:st)/
/(?i)te(?-i)st/
/(?i)te(?^)st/
/(?s)^.+$/
dot **.** matches line break
whole file start/end

## Gapture Group

\1 替代之前抓到的 group 1

`A: My name is (\w+). B: Hi \1!`

- 雙引號間的文字


- match between html tags
`(?s)(?<=<h(\d)>).*(?=<\/h\1)`

```
<h1>This is title</h1> some word <h2><span>abc</sp
an></h2> not important <h3> Match me! </h3>
```

需要處理換行

## Regex in Python

- re.findall()
- re.sub()
- re.split()

? re 有沒有 compile 的差別 [stack overflow](https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile)

-> 跑 findall 之前會都會 compile 一次 regex 當需要多次使用或是處理大量文本的時候推薦先 compile 一次

`r` row string notation

re 可以調整 match flags



```
>>> text = 'aAaAAa bbBBbb\nAAaaaAa BBBbbb'
>>> print(text)
aAaAAa bbBBbb
AAaaaAa BBBbbb
>>> re.findall(r'b+$', text, flags=re.M|re.I)
['bbBBbb', 'BBBbbb']
```

預設是 single line

### Grep

grep
egrep / grep -E -> basic regex
fgrep / grep -F
pcregrep -> 支援最多進階語法
pgrep -> grep process = ps | grep vim


# Reference

- [Regular Expressions Info](https://www.regular-expressions.info/refunicode.html)
- [grep manual](https://www.gnu.org/software/grep/manual/html_node/Regular-Expressions.html)

# Regex Games
* https://regexone.com/lesson/letters_and_digits
* https://alf.nu/RegexGolf
* http://play.inginf.units.it/#/level/1
