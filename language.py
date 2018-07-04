from collections import OrderedDict

favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'ruby',
   'phil': 'java',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): print(language.title())
print("_" *50)
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'ruby'
favorite_languages['sarah'] = 'python'
favorite_languages['edward']= 'c++'
favorite_languages['phil'] = 'java'
favorite_languages['loh'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "norm for " + language.title())
