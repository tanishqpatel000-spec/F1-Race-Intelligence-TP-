const demo = [
  {Driver:'Driver A',Team:'Team Red',Points:420},{Driver:'Driver B',Team:'Team Blue',Points:385},{Driver:'Driver C',Team:'Team Silver',Points:310},{Driver:'Driver D',Team:'Team Green',Points:265},{Driver:'Driver E',Team:'Team Red',Points:220},{Driver:'Driver F',Team:'Team Blue',Points:180}
];
let rows = demo;
function render(){
 const driver=document.getElementById('driverChart'), team=document.getElementById('teamChart'), body=document.querySelector('#dataTable tbody');
 const max=Math.max(...rows.map(r=>r.Points),1);
 driver.innerHTML=rows.slice().sort((a,b)=>b.Points-a.Points).map(r=>`<div class="bar-row"><span>${escapeHtml(r.Driver)}</span><div class="bar-track"><div class="bar-fill" style="width:${Math.max(1,r.Points/max*100)}%"></div></div><b>${r.Points}</b></div>`).join('');
 const teams={}; rows.forEach(r=>teams[r.Team]=(teams[r.Team]||0)+r.Points);
 const tmax=Math.max(...Object.values(teams),1);
 team.innerHTML=Object.entries(teams).sort((a,b)=>b[1]-a[1]).map(([name,val])=>`<div class="bar-row"><span>${escapeHtml(name)}</span><div class="bar-track"><div class="bar-fill" style="width:${val/tmax*100}%"></div></div><b>${val}</b></div>`).join('');
 body.innerHTML=rows.slice(0,8).map(r=>`<tr><td>${escapeHtml(r.Driver)}</td><td>${escapeHtml(r.Team)}</td><td>${r.Points}</td></tr>`).join('');
}
function escapeHtml(v){return String(v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
document.getElementById('csvFile').addEventListener('change',async e=>{const file=e.target.files[0];if(!file)return;const text=await file.text();const lines=text.trim().split(/\r?\n/);const headers=lines.shift().split(',').map(s=>s.trim().replace(/^"|"$/g,''));const idx={driver:headers.findIndex(h=>/driver|name/i.test(h)),team:headers.findIndex(h=>/team|constructor/i.test(h)),points:headers.findIndex(h=>/points|score/i.test(h))};if(idx.driver<0||idx.points<0){document.getElementById('fileStatus').textContent='CSV needs Driver and Points columns (Team is optional).';return;}const parsed=lines.map(line=>{const c=line.split(',').map(s=>s.trim().replace(/^"|"$/g,''));return{Driver:c[idx.driver],Team:idx.team>=0?c[idx.team]:'Unspecified',Points:Number(c[idx.points])};}).filter(r=>r.Driver&&Number.isFinite(r.Points));if(!parsed.length){document.getElementById('fileStatus').textContent='No usable rows found in CSV.';return;}rows=parsed;document.getElementById('fileStatus').textContent=`Loaded ${rows.length} records from ${file.name}`;render();});
document.getElementById('resetBtn').addEventListener('click',()=>{rows=demo;document.getElementById('csvFile').value='';document.getElementById('fileStatus').textContent='Showing illustrative demo data';render();});
render();
