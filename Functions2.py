# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# ex1
# def great():
#     mname = str(input())
#     for i in movies:
#         if (i["name"] == mname):
#             if (i["imdb"] > 5.5):
#                 return True
#             else:
#                 return False
# print(great())



#ex2
# def great():
#     print("This is your sublist: ")
#     for x in movies:
#         if (x["imdb"] > 5.5):
#             print(x)
# great()




#ex3
# def great():
#     chosen_cat = str(input())
#     for i in movies:
#         for x in i:
#             if (i[x] == chosen_cat):
#                 print(i)
# great()


#ex4
# def great():
#     dict_length = len(movies)
#     total = 0
#     for i in movies:
#         total = total + i["imdb"]
#     print(total / dict_length)
# great()



#ex5
# def great():
#     chosen_cat = str(input())
#     total = 0
#     count = 0
#     for i in movies:
#         for x in i:
#             if (i[x] == chosen_cat):
#                 total = total + i["imdb"]
#                 count = count + 1
#     print(total / count)
# great()