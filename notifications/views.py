from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import json
from .models import FCMToken, InAppNotification


def create_FCM_token(request):
    data = json.loads(request.body)
    FCM_token_value = data["FCMToken"]
    # 새로운 token일 경우
    if not FCMToken.objects.filter(value=FCM_token_value).exists():
        new_token = FCMToken(value=FCM_token_value, user=request.user)
        new_token.save()
        return JsonResponse(True, safe=False)
    # 이미 등록된 token일 경우
    else:
        # 이미 등록된 token이지만 접속한 유저가 다른 경우, 다른 기기에서
        # 로그인한 유저 A가 유저 B가 등록한 기기에서 로그인한 것이다.
        return JsonResponse(False, safe=False)


def on_in_app_notification_clicked(request, pk):
    print("notification clicked!")
    notification = get_object_or_404(InAppNotification, pk=pk)
    notification.is_read = True
    notification.save()

    return redirect(notification.link)