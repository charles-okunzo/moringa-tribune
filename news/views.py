from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
  # return HttpResponse('Welcome to Moringa Tribune')
  return render(request, 'welcome.html', {'name': 'Charles'})


def news_of_day(request):
  date = dt.date.today()
  return render(request, 'all-news/today-news.html', {"date":date,})
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
    redirect(news_of_day)

  return render(request, 'all-news/passed-news.html', {"date": date})

  # return HttpResponse(html)




