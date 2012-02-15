# -*- charset: utf-8 -*-

import os
import urllib2
from BeautifulSoup import BeautifulSoup as bs


URL = "http://no.wikipedia.org/wiki/Norges_kommuner"

'''
Havest structure:

1. <tr>
2. <td>0101</td> 
3. <td><a href="/wiki/Halden" title="Halden">Halden</a></td>
4. <td><a href="/w/index.php?title=Halden_(adm.senter)&amp;action=edit&amp;redlink=1" class="new" title="Halden (adm.senter) (siden finnes ikke)">Halden</a></td>
5. <td><a href="/wiki/%C3%98stfold" title="Østfold">Østfold</a></td>
6. <td><span style="display:none">3&amp;504&amp;29547&amp;</span>29&#160;547</td>
7. <td>642,34</td>
8. <td>
9. <div class="center">
10. <div class="floatnone"><a href="/wiki/Fil:NO_0101_Halden.svg" class="image" title="Halden markert med rødt på fylkeskartet"><img alt="Halden markert med rødt på fylkeskartet" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/NO_0101_Halden.svg/45px-NO_0101_Halden.svg.png" width="45" height="59" /></a></div>
11. </div>
12. </td>
13. <td><a href="/wiki/Fil:Halden_komm.svg" class="image" title="Haldens kommunevåpen"><img alt="Haldens kommunevåpen" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Halden_komm.svg/46px-Halden_komm.svg.png" width="46" height="75" /></a></td>
14. <td><a href="/wiki/Bokm%C3%A5l" title="Bokmål">Bokmål</a></td>
15. <td><a href="/wiki/Thor_Edquist" title="Thor Edquist">Thor Edquist</a></td>
16. <td><a href="/wiki/H%C3%B8yre" title="Høyre">Høyre</a></td>
17. </tr>

Filen åpnes og avsluttes med en tr. Første tr brukes for å beskrive dataene, så denne kan fjernes
første td er kommunenummer, deretter navn, noe, fylke, koordinater, logo (last ned!), 
målform, ordfører, parti. 

Ta ned all data, for prosjektet er kommune, fylke, logo, innbyggertall, og størrelse viktig. Resten for moro skyld. 

+ Lage en norske kommuner side med all dataen kanskje? 
+ For prosjektet: Hente ut sjangerene fra kommunene og fylkene og normalisere disse 
slik at den prosentvise fordelingen dukker opp. Lage en lite raphael app med animasjon og listevalg.



'''