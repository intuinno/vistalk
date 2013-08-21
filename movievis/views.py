# Create your views here.

from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.http import HttpResponse
import json
from django.shortcuts import render, get_object_or_404
from django.core import serializers

from movievis.models import CommentState

def detail(request, comment_id):
    # comment = get_object_or_404(CommentState, pk=comment_id)
    comment = serializers.serialize('json',CommentState.objects.all())
    # return HttpResponse(json.dumps(comment.content), content_type="application/json")
    return HttpResponse(comment, content_type="application/json")

@csrf_exempt
def save_comment(request):
    if request.is_ajax():
        if request.method == 'POST':
            print 'Raw Data: "%s"' % request.body
            c = CommentState(content="thest",vis_state=request.body)
            c.save()

    return HttpResponse("OK")