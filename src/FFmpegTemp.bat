@echo off

REM ← の行はコメントです。
REM 
REM 【置換情報】
REM ツールによって置き換えされる文字列があります。
REM 仕様書\バッチ置換特殊定数一覧.html をご覧ください。
REM

REM ↓【例：番組名とURLを表示する】
echo 番組名：後藤沙緒里と喜多村英梨のSEラジオ
echo 回数：第3-4回
echo URL：https://vms-api.hibiki-radio.jp/api/v1/videos/playlist.m3u8?token=fAHi7H9hBw8W1Wyvmutje0fblokRLLZ1laMmqpNcBCA%%3D^&vms_video_id=372^&user_id=-1

title 後藤沙緒里と喜多村英梨のSEラジオ 第3-4回

REM ↓【例：ffmpegと連携する場合は以下のように記述します】
ffmpeg -i "https://vms-api.hibiki-radio.jp/api/v1/videos/playlist.m3u8?token=fAHi7H9hBw8W1Wyvmutje0fblokRLLZ1laMmqpNcBCA%%3D&vms_video_id=372&user_id=-1" -vcodec copy -acodec copy -bsf:a aac_adtstoasc "D:\WebRadio\HibikiTool300_beta7\download\後藤沙緒里と喜多村英梨のSEラジオ 第3-4回.mp4"

pause
