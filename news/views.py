from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
import datetime as dt
from news.email import send_welcome_email
from news.forms import NewsletterForm

from news.models import Article, NewsletterRecipient

# Create your views here.
# def welcome(request):
#   # return HttpResponse('Welcome to Moringa Tribune')
#   return render(request, 'welcome.html', {'name': 'Charles'})


def news_today(request):
  date = dt.date.today()
  news = Article.today_news()
  form = NewsletterForm()
  if request.method == 'POST':
    form = NewsletterForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['your_name']
      email = form.cleaned_data['email']
      recipient = NewsletterRecipient(name = name, email = email)
      recipient.save()
      send_welcome_email(name, email)
      HttpResponseRedirect('news_today')
      print('Valid!', request.POST)
  return render(request, 'all-news/today-news.html', {"date":date, "news":news, 'form':form})
  # day = convert_to_day(date)
  # html = f'''
  # <html>
  #           <body>
  #               <h1>{day} {date.day}-{date.month}-{date.year}</h1>
  #           </body>
  #       </html>
  # '''
  # return HttpResponse(html)


# def convert_to_day(date):
#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(date)

#     days = ["monday", 'tuesday', 'wednesday', 'thursday', 'friday', 'sartuday' 'sunday']
#     day = days[day_number]

#     return day

def past_days_news(request, past_date):
  try:
      #converts data from the string Url
    date = dt.datetime.strptime(past_date, '%Y-%m-%d')
    # # day = convert_to_day(date)

    # html = f'''
    # <html>
    #           <body>
    #               <h1>{day} {date.day}-{date.month}-{date.year}</h1>
    #           </body>
    #       </html>
    # '''
  except ValueError:
    # Raise 404 error when ValueError is thrown
    raise Http404()

  if date == dt.date.today():
    redirect(news_today)

  news = Article.days_news(date)

  return render(request, 'all-news/passed-news.html', {"date": date, "news":news})

  # return HttpResponse(html)



def search_results(request):
  if 'article' in request.GET and request.GET['article']:
    search_term = request.GET.get('article')
    searched_articles = Article.search_by_title(search_term)
    message = f'{search_term}'

    return render(request, 'all-news/search.html', {'articles': searched_articles, 'message':message})

  else:
    message = "You haven't searched for any term"

    return render(request, 'all-news/search.html',{"message":message})

def article(request, article_id):
  try:
    article = Article.objects.get(id=article_id)

  except ValueError:
    raise Http404

  return render(request, 'all-news/article.html', {'article': article})



