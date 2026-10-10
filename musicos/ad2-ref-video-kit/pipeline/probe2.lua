local S = "C:/Users/pmpel/projects/iglesia_el_renuevo/musicos/ad2-ref-video-kit/pipeline/"
local function log(s) local f=io.open(S.."probe2.log","a"); f:write(os.date("%H:%M:%S ")..s.."\n"); f:close() end
log("start")
reaper.Main_OnCommand(40859,0)
reaper.InsertTrackAtIndex(0,false)
local tr = reaper.GetTrack(0,0)
local fx = reaper.TrackFX_AddByName(tr,"VST3i: Addictive Drums 2 (XLN Audio)",false,-1)
log("fx "..tostring(fx))
local t0 = os.time()
local d8=false
local function dump(tag)
  local ok,chunk = reaper.GetTrackStateChunk(tr,"",false)
  local c = io.open(S.."chunk_"..tag..".txt","w"); c:write(chunk); c:close(); log("dumped "..tag.." "..#chunk)
end
local function loop()
  local dt = os.time()-t0
  if dt >= 25 then
    dump("25s")
    reaper.Main_SaveProjectEx(0,S.."probe2.rpp",0); log("saved")
    reaper.Main_OnCommand(40004,0)
  else
    if dt >= 8 and not d8 then d8=true; dump("8s") end
    reaper.defer(loop)
  end
end
log("loop")
reaper.defer(loop)
