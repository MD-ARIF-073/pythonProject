

import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "blue"):
   print("Match 3")


# উপরে আমরা একটি রেগুলার এক্সপ্রেশন ডিফাইন করেছি r"gr.y" এর মাধ্যমে। এখানে . দিয়ে ওই অবস্থানে যেকোনো ক্যারেক্টার এর সাথে ম্যাচ দেখতে বলা হয়েছে।
# আর তাই যখন grey বা gray এর সাথে ম্যাচ করা হয়েছে তখন রেজাল্ট সত্য এসেছে এবং একটি প্রিন্ট স্টেটমেন্ট এক্সিকিউট হয়েছে। blue এর ক্ষেত্রে তা হয় নি।

import re

pattern = r"^wr.te$"

if re.match(pattern, "write"):
   print("Match 1")

if re.match(pattern, "wrote"):
   print("Match 2")

if re.match(pattern, "writer"):
   print("Match 3")

# উপরের প্রোগ্রামে r"^wr.te$" এর মাধ্যমে একটি স্ট্রিং যার শুরু এবং শেষ নির্দিষ্ট অর্থাৎ যথাক্রমে w এবং e কিন্তু wr এর পর যেকোনো ক্যারেক্টার থাকতে পারে এবং সেটির পর আবার te থাকতে হবে। তাই write এবং wrote ম্যাচ করেছে।