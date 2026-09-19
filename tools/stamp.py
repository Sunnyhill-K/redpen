# 배포 직전에 index.html 의 <meta name="build"> 에 지금 시각(서울)을 적는다. 푸시 루틴에서 자동으로 부른다.
import re, datetime, zoneinfo, pathlib
p=pathlib.Path(__file__).resolve().parent.parent/'index.html'
s=p.read_text(encoding='utf-8')
now=datetime.datetime.now(zoneinfo.ZoneInfo('Asia/Seoul')).replace(microsecond=0).isoformat()
s2,n=re.subn(r'<meta name="build" content="[^"]*">', lambda m: '<meta name="build" content="'+now+'">', s, count=1)
assert n==1, 'build meta 가 없습니다'
p.write_text(s2, encoding='utf-8'); print('build', now)
