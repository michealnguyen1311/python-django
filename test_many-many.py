from myapp.models import Publication, Article
p1 = Publication.objects.create(title="Title1")
p2 = Publication.objects.create(title="Title2")
p3 = Publication.objects.create(title="Title3")
a1 = Article.objects.create(headline="Headline1")
a2 = Article.objects.create(headline="Headline2")
a3 = Article.objects.create(headline="Headline3")

a1.publications.all()
# <QuerySet []>
a1.publications.add(p1)
a1.publications.all()
# <QuerySet [<Publication: Title1 is a Publication>]>
a1.publications.add(p2,p3)
a1.publications.all()
# <QuerySet [<Publication: Title1 is a Publication>, <Publication: Title2 is a Publication>, <Publication: Title3 is a Publication>]>
p1.article_set.all()
# <QuerySet [<Article: Headline1 is a Article>]> 
p1.article_set.add(a2,a3)
p1.article_set.all()
# <QuerySet [<Article: Headline1 is a Article>, <Article: Headline2 is a Article>, <Article: Headline3 is a Article>]>