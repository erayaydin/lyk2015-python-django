from str_util import utils

print("Palindrome [True]: ",utils.is_palindrome("ece"))
print("Palindrome [False]: ",utils.is_palindrome("ecem"))

print("GenWord: ",utils.gen_word(["a", "b", "c"], 5))
print("GenWord: ",utils.gen_word(["a", "b", "c"], 5))

print("IsUrl [True]: ", utils.is_url("http://www.google.com/"))
print("IsUrl [False]: ", utils.is_url("ftp://google.com/"))

print("Title Make [Bak Bunu Dedim]: ", utils.title_make("bak bunu dedim"))

print("Zip Str [baakbüa haikçü yyookk]: ", utils.zip_str("baba akü yok", "akü hiç yok"))