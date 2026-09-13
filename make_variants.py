# 굳음 원인 분리용 사본 생성기 — index.html 을 고친 뒤 실행하면 사본들이 같은 코드로 다시 만들어진다
import re
s=open('index.html',encoding='utf-8').read()
def w(name, t): open(name,'w',encoding='utf-8').write(t); print(name, len(t)//1024, 'KB')
NOFONT=lambda t: re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\n?', '', t)
w('nofont.html', NOFONT(s))
i=s.index('<script>\n(function(){'); j=s.index('})();\n</script>', i)+len('})();\n</script>')
stub='<script>document.getElementById("main").innerHTML="<p style=\'padding:20px;font-size:18px\'>스크립트 없는 껍데기 · 열린 시각: "+new Date().toTimeString().slice(0,8)+"</p>";</script>'
nojs=s[:i]+stub+s[j:]; w('nojs.html', nojs); w('nofont-nojs.html', NOFONT(nojs))
w('noboot.html', s.replace("render();\nboot();", "render(); document.getElementById('main').insertAdjacentHTML('beforeend','<p style=\"padding:20px\">noboot · 열린 시각: '+new Date().toTimeString().slice(0,8)+'</p>');"))
w('noscroll.html', s.replace("window.scrollTo(", "((..._)=>{})("))
c=s.replace("if (window.ResizeObserver) new ResizeObserver(syncTop).observe($('.top'));\nif (document.fonts) document.fonts.ready.then(syncTop);\nwindow.addEventListener('load', syncTop);", "")
c=c.replace("if (window.ResizeObserver) new ResizeObserver(()=>fixBodyWidth()).observe(document.getElementById('main'));", "")
w('noobserve.html', c)
bi=s.index('async function boot(){'); bj=s.index('\n}\n', bi)+3
w('nonet.html', s[:bi]+"""async function boot(){
  cfg={v:2, iter:1, users:[{id:'t', name:'시험', role:'admin', salt:'', k:''}]}; role='editor'; me={id:'t', name:'시험', role:'admin'}; artifactNs={};
  applyRole(); cases=[]; render(); document.getElementById('main').insertAdjacentHTML('beforeend','<p style="padding:20px">nonet · 열린 시각: '+new Date().toTimeString().slice(0,8)+'</p>');
}
"""+s[bj:])
b8=s.replace("Kraw=ub64(sess.k); K=await importK(Kraw); esec=sess.s||null;", "Kraw=ub64(sess.k); K=null; esec=sess.s||null;")
b8=b8.replace("if (token && esec) Ke=await deriveKe(Kraw, esec); else if (token)", "if (token && esec) Ke=null; else if (token)")
w('nocrypto.html', b8)
b9=s.replace("tmark('로그인 상태 확인'); try { await loadIndex(); tmark('목록 읽음'); } catch(e){ toast('목록을 읽지 못했습니다: '+((e&&e.message)||e)); }", "tmark('로그인 상태 확인'); cases=[];")
assert b9!=s; w('noindex.html', b9)
# 설정 받기만 건너뜀(세션만으로 홈 그림). 목록은 받음
b10=s.replace("tmark('시작'); try { await loadConfig(); tmark('설정 읽음'); }", "tmark('시작'); try { cfg={v:2, iter:310000, users:[]}; tmark('설정 생략'); }")
assert b10!=s; w('noconfig.html', b10)
