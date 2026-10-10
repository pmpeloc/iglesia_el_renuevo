-- ponytail: file-polling command server inside REAPER. cmd.txt -> executes -> done.txt
local S = "C:/Users/pmpel/projects/iglesia_el_renuevo/musicos/ad2-ref-video-kit/pipeline/"
local function log(s) local f=io.open(S.."server.log","a"); f:write(os.date("%H:%M:%S ")..s.."\n"); f:close() end
local function readf(p) local f=io.open(p,"rb"); if not f then return nil end; local d=f:read("a"); f:close(); return d end
local function writef(p,d) local f=io.open(p,"wb"); f:write(d); f:close() end
local function track()
  local tr = reaper.GetTrack(0,0)
  if not tr then reaper.InsertTrackAtIndex(0,false); tr=reaper.GetTrack(0,0) end
  return tr
end
local function ensure_fx(tr)
  local fx = reaper.TrackFX_GetByName(tr,"VST3i: Addictive Drums 2 (XLN Audio)",false)
  if fx < 0 then fx = reaper.TrackFX_AddByName(tr,"VST3i: Addictive Drums 2 (XLN Audio)",false,-1) end
  return fx
end
local cmds = {}
function cmds.dump(args) local tr=track(); ensure_fx(tr); local _,c=reaper.GetTrackStateChunk(tr,"",false); writef(args[1],c); return "dumped "..#c end
function cmds.setchunk(args) local tr=track(); local c=readf(args[1]); local ok=reaper.SetTrackStateChunk(tr,c,false); return "setchunk "..tostring(ok) end
function cmds.midi(args) -- args: file with lines "start_sec note vel dur_sec"
  local tr=track()
  for i=reaper.CountTrackMediaItems(tr)-1,0,-1 do reaper.DeleteTrackMediaItem(tr,reaper.GetTrackMediaItem(tr,i)) end
  local len=tonumber(args[2]) or 4
  local it=reaper.CreateNewMIDIItemInProj(tr,0,len,false); local take=reaper.GetActiveTake(it)
  local n=0
  for line in readf(args[1]):gmatch("[^\r\n]+") do
    local t,note,vel,dur=line:match("([%d%.]+)%s+(%d+)%s+(%d+)%s+([%d%.]+)")
    if t then
      local sp=reaper.MIDI_GetPPQPosFromProjTime(take,tonumber(t)); local ep=reaper.MIDI_GetPPQPosFromProjTime(take,tonumber(t)+tonumber(dur))
      reaper.MIDI_InsertNote(take,false,false,sp,ep,0,tonumber(note),tonumber(vel),true); n=n+1
    end
  end
  reaper.MIDI_Sort(take)
  reaper.GetSet_LoopTimeRange(true,false,0,len,false)
  return "midi notes "..n
end
function cmds.render(args) -- args: out wav path (absolute, no ext)
  local dir,name=args[1]:match("^(.*)/([^/]+)$")
  reaper.GetSetProjectInfo_String(0,"RENDER_FILE",dir,true)
  reaper.GetSetProjectInfo_String(0,"RENDER_PATTERN",name,true)
  reaper.GetSetProjectInfo(0,"RENDER_SETTINGS",0,true)      -- master mix
  reaper.GetSetProjectInfo(0,"RENDER_BOUNDSFLAG",2,true)    -- time selection
  reaper.GetSetProjectInfo(0,"RENDER_CHANNELS",2,true)
  reaper.GetSetProjectInfo(0,"RENDER_SRATE",44100,true)
  reaper.GetSetProjectInfo(0,"RENDER_ADDTOPROJ",0,true)
  reaper.GetSetProjectInfo(0,"RENDER_DITHER",0,true)
  reaper.GetSetProjectInfo(0,"RENDER_TAILFLAG",0,true)
  reaper.GetSetProjectInfo_String(0,"RENDER_FORMAT","ZXZhdxgAAA==",true) -- wav 24-bit
  reaper.Main_OnCommand(42230,0) -- render using most recent settings, auto-close
  return "rendered "..args[1]
end
function cmds.eval(args) local f=assert(loadfile(args[1])); return tostring(f(track(),ensure_fx(track()))) end
function cmds.save(args) reaper.Main_SaveProjectEx(0,args[1],0); return "saved" end
function cmds.quit() reaper.Main_SaveProjectEx(0,S.."server_last.rpp",0); reaper.Main_OnCommand(40004,0); return "quit" end
local function loop()
  local c = readf(S.."cmd.txt")
  if c and #c>0 then
    os.remove(S.."cmd.txt")
    local args={}; for w in c:gmatch("%S+") do args[#args+1]=w end
    local name=table.remove(args,1)
    local ok,res = pcall(function() return cmds[name](args) end)
    log(name.." -> "..tostring(res)); writef(S.."done.txt",tostring(ok).." "..tostring(res))
  end
  reaper.defer(loop)
end
log("server up"); reaper.defer(loop)
