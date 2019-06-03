# A-modest-look-at-Cryptojacking

Formato páginas analizadas:
nombreArchivo; cpuChromium; cpuTotal; ramUsada; kilobytesEnviados; kilobytesRecibidos

###Páginas limpias
'facebook.com'.txt; 0.01; 10.03; 48.7; 2069471.0; 15134243.0
'github.com'.txt; 0.0; 7.1; 47.79; 2077355.0; 15153483.0
'google.com'.txt; 0.0; 7.22; 47.61; 2071444.0; 15143375.0
'mail.google.com'.txt; 0.0; 13.86; 47.8; 2085351.0; 15171254.0
'twitter.com'.txt; 0.0; 6.57; 48.37; 2080263.0; 15163034.0
'www.instagram.com'.txt; 0.0; 14.79; 47.71; 2083223.0; 15167742.0
'youtube.com'.txt; 2.21; 18.34; 51.12; 2066103.0; 15119288.0

###Páginas potencialmente mineras
'cinemametropolitan.it'.txt; 15.46; 24.91; 56.25; 2167965.0; 16197850.0
'doorbin.net'.txt; 7.71; 37.22; 49.27; 2286510.0; 18016781.0
'englishnews.thegoan.net'.txt; 6.69; 13.58; 49.48; 2256920.0; 17218740.0
'forex-trading.hol.es'.txt; 18.85; 35.92; 50.75; 2100648.0; 15232837.0
'hydraulica-ua.com'.txt; 7.61; 60.96; 53.82; 2197833.0; 16681167.0
'iaijiu.com'.txt; 19.89; 33.11; 39.63; 2299583.0; 18173037.0
'mymarriage.co.za'.txt; 2.49; 8.68; 55.32; 2144149.0; 15726524.0
'no'.txt; 2.04; 10.7; 55.36; 2144624.0; 15729358.0
'onepace.net'.txt; 8.6; 18.87; 51.82; 2278018.0; 17836075.0
'peliculashd.site'.txt; 17.54; 37.03; 50.48; 2230936.0; 16908993.0
'pimpmylevel.cryptdough.co.uk'.txt; 5.99; 17.04; 49.95; 2221687.0; 16759572.0
'piratebayproxy247.org'.txt; 0.7; 11.52; 49.51; 2090182.0; 15181647.0
'pra.open.tips'.txt; 7.24; 10.93; 50.87; 2176870.0; 16313498.0
'redbitcoins.net'.txt; 9.81; 33.93; 54.86; 2241973.0; 17041536.0
'sj2s.hostei.com'.txt; 3.39; 8.84; 50.31; 2172670.0; 16281544.0
'studyenglishgenius.com'.txt; 6.67; 21.26; 51.33; 2215608.0; 16747996.0
'tommyhulihanbasketball.com'.txt; 11.16; 15.99; 48.9; 2113771.0; 15365433.0
'www.thehopepage.org'.txt; 0.66; 6.95; 54.82; 2140592.0; 15670808.0
'www5.fmovie.cc'.txt; 2.95; 11.7; 52.59; 2185061.0; 16413305.0

Se aplicó el promedio de uso de cpu en chromium por cada página, el uso de cpu total y el de ram por instantes de tiempo un total de 100 veces por cada página. Se puso en una lista las páginas que se consideraban benignas y en otro las que se encontraban sospechosamente mineras. En las benignas, casi ninguna superó el 1% del uso de los procesos lógicos, mientras que en las potencialmente mineras, casi la mitad sobrepasaba el 10%. Una página que no debería hacer nada más que cargar información para ser mostrada, rápidamente pasa a dejar el uso de los núcleos, lo que hace que los links limpios bajen su promedio de uso a un 0% en poco más de 1 minuto. De estos datos se puede evidenciar que la página más sospechosa de ser minera es la de peliculashd.site. Otro aspecto a tener en cuenta es que las páginas que cargan videos suelen ser las que más procesamiento utiliza, sin embargo, si comparamos a youtube.com con peliculashd.site, nos damos cuenta que la diferencia es de aproximadamente el 800% de una con respecto a la otra. En el uso total de CPU algunos promedios llegaron hasta el 60%, esto puede deberse a que el antivirus estuviera en constante chequeo de esta página maliciosa (Se puede descartar la posibilidad de ejecución de otro programa ya que el algoritmo se corrió en condiciones óptimas, es decir, ningún otro programa abierto). En el uso de ram se puede observar valores que varían entre el 47.71 y el 51.12 para las limpias, y entre el 49.27 y 56.25 para las mineras, lo que indica una diferencia no muy relevante en términos de porcentaje.

Integrantes:
Luis Fernando Munoz
Leonardo Franco
Camilo Sepulveda