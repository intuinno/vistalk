# Create your views here.

from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.http import HttpResponse
import json
from django.shortcuts import render, get_object_or_404
from django.core import serializers

# 
# def detail(request, comment_id):
#     comment = get_object_or_404(MovievisCommentState, pk=comment_id)
#     # comment = json.dumps(CommentState.objects.get(pk=comment_id))
#     # return HttpResponse(json.dumps(comment.content), content_type="application/json")
#     return render(request, 'movievis/detail.html', { 'comment':comment})
# 
# @csrf_exempt
# def save_comment(request):
#     if request.is_ajax():
#         if request.method == 'POST':
#             print 'Raw Data: "%s"' % request.body
#             c = MovievisCommentState(content="thest",vis_state=request.body)
#             c.save()
# 
#     return HttpResponse("OK")