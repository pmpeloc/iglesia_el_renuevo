-- eval helper: reads midi_spec.txt (line1: length_sec; then "t note vel dur")
local tr,fx=...
local S="C:/Users/pmpel/projects/iglesia_el_renuevo/musicos/ad2-ref-video-kit/pipeline/"
local f=io.open(S.."midi_spec.txt"); local spec=f:read("a"); f:close()
for i=reaper.CountTrackMediaItems(tr)-1,0,-1 do reaper.DeleteTrackMediaItem(tr,reaper.GetTrackMediaItem(tr,i)) end
local len=tonumber(spec:match("^([%d%.]+)"))
local it=reaper.CreateNewMIDIItemInProj(tr,0,len,false); local take=reaper.GetActiveTake(it); local n=0
for line in spec:gmatch("[^\r\n]+") do
  local t,note,vel,dur=line:match("^([%d%.]+)%s+(%d+)%s+(%d+)%s+([%d%.]+)")
  if t then
    local sp=reaper.MIDI_GetPPQPosFromProjTime(take,tonumber(t)); local ep=reaper.MIDI_GetPPQPosFromProjTime(take,tonumber(t)+tonumber(dur))
    reaper.MIDI_InsertNote(take,false,false,sp,ep,0,tonumber(note),tonumber(vel),true); n=n+1
  end
end
reaper.MIDI_Sort(take); reaper.GetSet_LoopTimeRange(true,false,0,len,false); reaper.UpdateArrange()
return "midi notes "..n.." len "..len
