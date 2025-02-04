from django.http import HttpResponse


def homePageView(respoce):
  return HttpResponse("hello, world")