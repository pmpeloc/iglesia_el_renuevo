local S = "C:/Users/pmpel/projects/iglesia_el_renuevo/musicos/ad2-ref-video-kit/pipeline/"
local out = io.open(S.."probe_out.txt","w")
reaper.Main_OnCommand(40859,0) -- new project tab
reaper.InsertTrackAtIndex(0,false)
local tr = reaper.GetTrack(0,0)
local fx = reaper.TrackFX_AddByName(tr,"VST3i: Addictive Drums 2 (XLN Audio)",false,-1)
out:write("fx index "..tostring(fx).."\n")
if fx>=0 then
  local n = reaper.TrackFX_GetNumParams(tr,fx)
  out:write("numparams "..n.."\n")
  for i=0,n-1 do
    local _,name = reaper.TrackFX_GetParamName(tr,fx,i,"")
    local v,mn,mx = reaper.TrackFX_GetParam(tr,fx,i)
    local _,fmt = reaper.TrackFX_GetFormattedParamValue(tr,fx,i,"")
    out:write(string.format("%d\t%s\t%.4f\t[%g..%g]\t%s\n",i,name,v,mn,mx,fmt))
  end
  local _,pname = reaper.TrackFX_GetPreset(tr,fx,"")
  out:write("preset: "..tostring(pname).."\n")
  local _,np = reaper.TrackFX_GetPresetIndex(tr,fx)
  out:write("presetcount: "..tostring(np).."\n")
  local ok,chunk = reaper.GetTrackStateChunk(tr,"",false)
  local c = io.open(S.."chunk.txt","w"); c:write(chunk); c:close()
end
out:close()
reaper.Main_SaveProjectEx(0,S.."probe.rpp",0)
reaper.Main_OnCommand(40004,0) -- quit
