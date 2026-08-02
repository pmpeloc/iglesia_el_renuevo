# Raíces MVP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Entregar una PWA privada, segura y medible para probar durante una semana con un joven y un líder, y luego habilitarla para 30 jóvenes y 10 líderes sin rehacer su arquitectura.

**Architecture:** Una aplicación Next.js App Router desplegada en Vercel usa Supabase para autenticación, Postgres, RLS, archivos, funciones programadas y notificaciones. El progreso, los permisos y las publicaciones se confirman siempre en el servidor. OpenAI y Adobe sólo se invocan desde funciones protegidas para producir borradores que un administrador debe revisar; ningún contenido generado se publica automáticamente.

**Tech Stack:** Next.js 16, React 19, TypeScript, CSS nativo, Supabase Auth/Postgres/Storage/Edge Functions/Cron, OpenAI Responses API (`gpt-5.6-terra`), GPT Image 2, OpenAI TTS (`tts-1`), Adobe PDF Extract, Web Push, Vitest, Testing Library, pgTAP y Playwright.

## Global Constraints

- Ejecutar los comandos desde `red_jovenes/`, salvo que un paso indique otra carpeta.
- La aplicación nueva vive en `raices/`. No modificar los sermones, mockups ni documentos ajenos.
- El árbol de trabajo ya contiene cambios del usuario: nunca usar `git add .`; agregar sólo las rutas listadas en cada tarea.
- Mantener Railway fuera del MVP. Vercel sirve la PWA y Supabase cubre el backend.
- No agregar librerías de componentes, animación, estado global, gráficos, PDF flip ni PWA. Usar React, CSS, APIs del navegador y Postgres.
- No calcular puntos de forma optimista. La interfaz muestra el progreso sólo después de que la RPC transaccional confirme la escritura.
- La planta nunca pierde estado por inactividad. No existe ranking individual ni “puntaje espiritual”.
- Las métricas comunitarias nunca incluyen nombres, minutos personales ni porcentajes públicos de personas atrasadas.
- Toda nota es privada salvo una acción explícita y reversible para compartirla con el líder asignado.
- Las métricas públicas no muestran agregados de menos de cinco jóvenes para evitar inferencias durante el piloto.
- Ninguna clave de OpenAI, Adobe, VAPID o `service_role` llega al navegador.
- Cada paquete generado por IA comienza en `draft`; sólo una transacción iniciada por un administrador puede publicarlo.

## Delivery Gates

1. **Gate A — Piloto funcional:** tareas 1–6. Permite probar acceso, onboarding, misión, recuperación, planta, diario y acompañamiento.
2. **Gate B — Comunidad y recursos:** tareas 7–10. Agrega oración, colecciones, biblioteca, modo adaptativo y recordatorios.
3. **Gate C — Fábrica editorial:** tareas 11–13. Agrega corpus, perfil doctrinal, generación, revisión y medios.
4. **Gate D — Lanzamiento:** tareas 14–15. Cierra accesibilidad, seguridad, despliegue y protocolo de prueba.

## File Map

```text
raices/
├── .env.example
├── package.json
├── next.config.ts
├── playwright.config.ts
├── vitest.config.ts
├── public/
│   ├── manifest.webmanifest
│   ├── sw.js
│   ├── offline.html
│   └── icons/{icon-192.png,icon-512.png}
├── scripts/
│   └── import-corpus.mjs
├── src/
│   ├── app/
│   │   ├── (auth)/login/page.tsx
│   │   ├── (app)/{page.tsx,camino/page.tsx,oracion/page.tsx,colecciones/page.tsx,biblioteca/page.tsx,mas/page.tsx}
│   │   ├── admin/{page.tsx,contenido/page.tsx,biblioteca/page.tsx}
│   │   ├── auth/callback/route.ts
│   │   ├── onboarding/page.tsx
│   │   ├── globals.css
│   │   └── layout.tsx
│   ├── components/{app-shell.tsx,plant.tsx,mission-card.tsx,prayer-wall.tsx,book-reader.tsx,push-opt-in.tsx}
│   ├── lib/
│   │   ├── auth/{actions.ts,guards.ts}
│   │   ├── domain/onboarding.ts
│   │   ├── supabase/{client.ts,server.ts,proxy.ts}
│   │   └── validation/{content.ts,prayer.ts}
│   └── proxy.ts
├── supabase/
│   ├── config.toml
│   ├── functions/
│   │   ├── _shared/{admin.ts,http.ts,openai.ts}
│   │   ├── generate-editorial-profile/index.ts
│   │   ├── generate-package/index.ts
│   │   ├── generate-media/index.ts
│   │   ├── process-books/index.ts
│   │   └── send-reminders/index.ts
│   ├── migrations/0001_identities.sql through 0011_media_assets.sql
│   └── tests/database/*.test.sql
└── tests/{unit,integration,e2e}/
```

---

### Task 1: Scaffold the installable PWA shell

**Files:**
- Create: `raices/package.json`
- Create: `raices/package-lock.json`
- Create: `raices/next.config.ts`
- Create: `raices/vitest.config.ts`
- Create: `raices/src/app/layout.tsx`
- Create: `raices/src/app/page.tsx`
- Create: `raices/src/app/globals.css`
- Create: `raices/src/components/app-shell.tsx`
- Create: `raices/public/manifest.webmanifest`
- Create: `raices/public/icons/icon-192.png`
- Create: `raices/public/icons/icon-512.png`
- Test: `raices/tests/unit/app-shell.test.tsx`

**Interfaces:**
- Consumes: los mockups aprobados en `output/mockups/raices/` y el nombre “Raíces”.
- Produces: shell móvil instalable, tokens visuales, navegación inferior y base de pruebas.

- [ ] **Step 1: Generate the minimal Next.js app**

```powershell
npx create-next-app@latest raices --ts --eslint --app --src-dir --import-alias "@/*" --use-npm --no-tailwind
Set-Location raices
npm install @supabase/supabase-js @supabase/ssr zod
npm install -D vitest jsdom @testing-library/react @testing-library/jest-dom @playwright/test @axe-core/playwright supabase
Set-Location ..
```

Remove the generated demo assets and keep only the files listed above. Add these scripts to `package.json`:

```json
{
  "test": "vitest run",
  "test:db": "supabase test db",
  "test:e2e": "playwright test",
  "typecheck": "tsc --noEmit",
  "check": "npm run lint && npm run typecheck && npm test && npm run build"
}
```

- [ ] **Step 2: Write the failing shell test**

```tsx
// raices/tests/unit/app-shell.test.tsx
import '@testing-library/jest-dom/vitest'
import { render, screen } from '@testing-library/react'
import { AppShell } from '@/components/app-shell'

it('identifies Raíces and exposes the five primary destinations', () => {
  render(<AppShell><p>Hoy</p></AppShell>)
  expect(screen.getByRole('banner')).toHaveTextContent('Raíces')
  for (const name of ['Inicio', 'Camino', 'Oración', 'Colecciones', 'Más']) {
    expect(screen.getByRole('link', { name })).toBeVisible()
  }
})
```

- [ ] **Step 3: Run it and confirm it fails**

Run: `npm --prefix raices test -- app-shell.test.tsx`

Expected: FAIL because `@/components/app-shell` does not exist.

- [ ] **Step 4: Implement the smallest accessible shell**

```tsx
// raices/src/components/app-shell.tsx
import Link from 'next/link'
import type { ReactNode } from 'react'

const destinations = [
  ['Inicio', '/'], ['Camino', '/camino'], ['Oración', '/oracion'],
  ['Colecciones', '/colecciones'], ['Más', '/mas'],
] as const

export function AppShell({ children }: { children: ReactNode }) {
  return <div className="app-shell">
    <header><strong>Raíces</strong></header>
    <main>{children}</main>
    <nav aria-label="Navegación principal">
      {destinations.map(([label, href]) => <Link key={href} href={href}>{label}</Link>)}
    </nav>
  </div>
}
```

Use CSS custom properties for the approved earth/green/gold palette, 44px minimum targets, visible focus, `prefers-reduced-motion`, safe-area padding and a `max-width: 480px` content rail. Add the manifest metadata in `layout.tsx`. Export the approved sprout mark directly as 192px and 512px PNG files; do not add an icon generator.

- [ ] **Step 5: Verify**

Run: `npm --prefix raices test -- app-shell.test.tsx && npm --prefix raices run lint && npm --prefix raices run build`

Expected: all commands exit 0; `/` renders with the five links and manifest metadata.

- [ ] **Step 6: Commit only the scaffold**

```powershell
git add raices/package.json raices/package-lock.json raices/next.config.ts raices/vitest.config.ts raices/src raices/public raices/tests/unit/app-shell.test.tsx
git commit -m "feat(raices): crear base PWA"
```

---

### Task 2: Create identities, assignments and database-enforced privacy

**Files:**
- Create: `raices/supabase/config.toml`
- Create: `raices/supabase/migrations/0001_identities.sql`
- Test: `raices/supabase/tests/database/0001_identities_rls.test.sql`
- Create: `raices/src/lib/database.types.ts`

**Interfaces:**
- Consumes: `auth.users` from Supabase Auth.
- Produces: `profiles`, `leader_assignments`, role helpers and RLS guarantees used by every later feature.

- [ ] **Step 1: Initialize Supabase and write the failing pgTAP privacy test**

Run: `npm --prefix raices exec supabase -- init`

The test creates one admin, two leaders and two young users, then asserts:

```sql
select plan(5);
select isnt((select public.is_admin('10000000-0000-0000-0000-000000000003')), true,
  'a young user is never an admin');
select results_eq(
  $$ select count(*) from public.leader_assignments where leader_id = auth.uid() $$,
  array[1::bigint], 'leader sees only own assignments');
select throws_ok(
  $$ update public.profiles set role = 'admin' where id = auth.uid() $$,
  '42501', null, 'user cannot elevate own role');
select lives_ok(
  $$ select id, display_name from public.profiles where id = auth.uid() $$,
  'user can read own profile');
select results_eq(
  $$ select count(*) from public.profiles where id <> auth.uid() $$,
  array[0::bigint], 'young user cannot browse profiles');
```

- [ ] **Step 2: Run it and confirm it fails**

Run: `npm --prefix raices run test:db`

Expected: FAIL because the tables and helpers do not exist.

- [ ] **Step 3: Add the identity schema and strict RLS**

```sql
create type public.app_role as enum ('young', 'leader', 'admin');

create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text not null check (char_length(display_name) between 2 and 60),
  role public.app_role not null default 'young',
  timezone text not null default 'America/Argentina/Buenos_Aires',
  created_at timestamptz not null default now()
);

create table public.leader_assignments (
  young_id uuid primary key references public.profiles(id) on delete cascade,
  leader_id uuid not null references public.profiles(id) on delete restrict,
  created_at timestamptz not null default now(),
  check (young_id <> leader_id)
);

create function public.current_role() returns public.app_role
language sql stable security definer set search_path = ''
as $$ select role from public.profiles where id = auth.uid() $$;

create function public.is_admin(candidate uuid default auth.uid()) returns boolean
language sql stable security definer set search_path = ''
as $$ select coalesce((select role = 'admin' from public.profiles where id = candidate), false) $$;
```

Add a `handle_new_user` trigger that inserts only `display_name` and the fixed role `young`; never accept a role from signup metadata. Enable RLS on both tables. Grant young users only their own profile, leaders their own profile plus assigned names, and admins all rows. Only admins may create assignments or change roles.

Add a `validate_leader_assignment` trigger that rejects an assignment unless `young_id` has role `young` and `leader_id` has role `leader`; the primary key already guarantees exactly one assigned leader per young user.

- [ ] **Step 4: Verify policies and generate types**

Run: `npm --prefix raices run test:db`

Expected: 5 pgTAP assertions pass.

Run: `npm --prefix raices exec supabase -- gen types typescript --local > raices/src/lib/database.types.ts`

- [ ] **Step 5: Commit**

```powershell
git add raices/supabase/config.toml raices/supabase/migrations/0001_identities.sql raices/supabase/tests/database/0001_identities_rls.test.sql raices/src/lib/database.types.ts raices/package.json raices/package-lock.json
git commit -m "feat(raices): proteger identidades y asignaciones"
```

---

### Task 3: Add mandatory Google and password authentication

**Files:**
- Create: `raices/.env.example`
- Create: `raices/src/lib/supabase/client.ts`
- Create: `raices/src/lib/supabase/server.ts`
- Create: `raices/src/lib/supabase/proxy.ts`
- Create: `raices/src/proxy.ts`
- Create: `raices/src/lib/auth/actions.ts`
- Create: `raices/src/lib/auth/guards.ts`
- Create: `raices/src/app/(auth)/login/page.tsx`
- Create: `raices/src/app/auth/callback/route.ts`
- Test: `raices/tests/unit/auth-redirect.test.ts`
- Test: `raices/tests/e2e/auth.spec.ts`

**Interfaces:**
- Consumes: Supabase publishable URL/key and the identity schema.
- Produces: cookie-based PKCE session, Google login, email/password signup/login and role-aware route protection.

- [ ] **Step 1: Write the failing redirect test**

```ts
import { destinationFor } from '@/lib/auth/guards'

it('routes authenticated users to the first unfinished requirement', () => {
  expect(destinationFor(null, false)).toBe('/login')
  expect(destinationFor('young', false)).toBe('/onboarding')
  expect(destinationFor('young', true)).toBe('/')
  expect(destinationFor('admin', true)).toBe('/admin')
})
```

- [ ] **Step 2: Confirm failure**

Run: `npm --prefix raices test -- auth-redirect.test.ts`

Expected: FAIL because `destinationFor` is missing.

- [ ] **Step 3: Implement clients, callback and actions**

Use `@supabase/ssr` with `createBrowserClient` and `createServerClient`. In `src/proxy.ts`, call `getClaims()`, propagate every cookie and response header supplied by `setAll`, and match all routes except static assets. Protected Server Components still call `getClaims()` and `current_role()`; Proxy is only an early redirect, not the authorization boundary.

```ts
export function destinationFor(role: 'young'|'leader'|'admin'|null, onboarded: boolean) {
  if (!role) return '/login'
  if (role === 'admin') return '/admin'
  return onboarded ? '/' : '/onboarding'
}
```

The login page contains:

- “Continuar con Google”.
- Email and password fields.
- Separate login and registration actions.
- Generic failure text that does not reveal whether an email exists.

`.env.example` contains names only: `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY`.

- [ ] **Step 4: Verify unit and browser flows**

Run: `npm --prefix raices test -- auth-redirect.test.ts`

Expected: PASS.

Run: `npm --prefix raices run test:e2e -- auth.spec.ts`

Expected: una visita anónima a `/` termina en `/login`; el callback inválido vuelve al login sin filtrar detalles.

- [ ] **Step 5: Commit**

```powershell
git add raices/.env.example raices/src/lib/supabase raices/src/lib/auth raices/src/proxy.ts 'raices/src/app/(auth)' raices/src/app/auth raices/tests/unit/auth-redirect.test.ts raices/tests/e2e/auth.spec.ts
git commit -m "feat(raices): agregar acceso obligatorio"
```

---

### Task 4: Onboard users and assign an approved plan

**Files:**
- Create: `raices/supabase/migrations/0002_onboarding_and_plans.sql`
- Test: `raices/supabase/tests/database/0002_onboarding.test.sql`
- Create: `raices/src/lib/domain/onboarding.ts`
- Create: `raices/src/app/onboarding/page.tsx`
- Test: `raices/tests/unit/onboarding.test.ts`
- Test: `raices/tests/e2e/onboarding.spec.ts`

**Interfaces:**
- Consumes: authenticated young user and at least one admin-approved plan.
- Produces: bounded onboarding answers, deterministic recommendation and confirmed `user_plan`.

- [ ] **Step 1: Write failing recommendation tests**

```ts
import { scorePlan } from '@/lib/domain/onboarding'

it('prefers a published plan matching focus, time and intensity', () => {
  const answers = { growthAreas: ['ansiedad'], dailyMinutes: 10, intensity: 'suave' as const }
  expect(scorePlan(answers, { focusTags: ['ansiedad'], minutes: 10, intensity: 'suave' })).toBe(4)
  expect(scorePlan(answers, { focusTags: ['liderazgo'], minutes: 20, intensity: 'intensa' })).toBe(0)
})
```

- [ ] **Step 2: Confirm failure**

Run: `npm --prefix raices test -- onboarding.test.ts`

Expected: FAIL because the scorer does not exist.

- [ ] **Step 3: Add schema, constraints and RLS**

Create:

- `onboarding_profiles`: one row per user; reading experience, prayer frequency, growth areas, 5/10/15 minutes, reminder time, intensity and completion timestamp.
- `plans`: title, summary, focus tags, minutes, intensity, status (`draft|published|archived`) and audit timestamps.
- `plan_missions`: exactly five ordered missions per week plus full and two-minute recovery content.
- `user_plans`: one active plan per user, start date and status.

RLS: users manage only their onboarding row and see only published plans; only admins write plans/missions; user plan creation uses an RPC that rejects draft plans.

```sql
create function public.confirm_recommended_plan(chosen_plan uuid)
returns uuid language plpgsql security definer set search_path = '' as $$
begin
  if not exists (select 1 from public.plans where id = chosen_plan and status = 'published') then
    raise exception 'plan_not_available';
  end if;
  insert into public.user_plans(user_id, plan_id, started_at, status)
  values (auth.uid(), chosen_plan, current_date, 'active')
  on conflict (user_id) where status = 'active' do update set plan_id = excluded.plan_id;
  return chosen_plan;
end $$;
```

- [ ] **Step 4: Implement the six-question onboarding**

Use native radios, checkboxes and time input. Present the best-scoring published plan, explain why it was selected, and allow choosing another published plan before confirmation. Do not collect mental-health, trauma, sin-confession or diagnostic data.

- [ ] **Step 5: Verify**

Run: `npm --prefix raices test -- onboarding.test.ts`

Run: `npm --prefix raices run test:db`

Run: `npm --prefix raices run test:e2e -- onboarding.spec.ts`

Expected: all pass; a draft plan cannot be assigned, a published plan can, and the user may adjust the recommendation.

- [ ] **Step 6: Commit**

```powershell
git add raices/supabase/migrations/0002_onboarding_and_plans.sql raices/supabase/tests/database/0002_onboarding.test.sql raices/src/lib/domain/onboarding.ts raices/src/app/onboarding raices/tests/unit/onboarding.test.ts raices/tests/e2e/onboarding.spec.ts
git commit -m "feat(raices): incorporar onboarding y planes"
```

---

### Task 5: Build the mission, recovery, plant and private journal loop

**Files:**
- Create: `raices/supabase/migrations/0003_progress_and_journal.sql`
- Test: `raices/supabase/tests/database/0003_progress_rls.test.sql`
- Create: `raices/src/components/plant.tsx`
- Create: `raices/src/components/mission-card.tsx`
- Create: `raices/src/app/(app)/page.tsx`
- Create: `raices/src/app/(app)/camino/page.tsx`
- Test: `raices/tests/e2e/mission.spec.ts`

**Interfaces:**
- Consumes: active user plan with five weekly missions.
- Produces: idempotent completion, server-confirmed points, non-regressive plant, recovery mode and journal sharing toggle.

- [ ] **Step 1: Write failing pgTAP progress tests**

Test the five stage thresholds `0, 50, 150, 300, 600`, reject negative mission points, submit the same mission twice and assert one completion, attempt a mission outside the active plan and assert rejection, and prove that inactivity never deletes points or reduces the returned stage.

- [ ] **Step 2: Confirm failure**

Run: `npm --prefix raices run test:db`

- [ ] **Step 3: Add atomic progress and journal storage**

Create `mission_completions` with primary key `(user_id, mission_id)`, mode `full|recovery`, confirmed points and timestamp. Create `journal_entries` with `shared_with_leader_at nullable`. Add:

```sql
create function public.complete_mission(target_mission uuid, completion_mode text)
returns table(total_points integer, plant_stage integer)
language plpgsql security definer set search_path = '' as $$
declare awarded integer;
begin
  select case when completion_mode = 'recovery' then m.recovery_points else m.points end
    into awarded
    from public.plan_missions m
    join public.user_plans up on up.plan_id = m.plan_id
    where m.id = target_mission
      and up.user_id = auth.uid()
      and up.status = 'active'
      and completion_mode in ('full','recovery');
  if awarded is null then raise exception 'invalid_mission'; end if;
  insert into public.mission_completions(user_id, mission_id, mode, points)
  values (auth.uid(), target_mission, completion_mode, awarded)
  on conflict (user_id, mission_id) do nothing;
  return query select p, case when p>=600 then 4 when p>=300 then 3 when p>=150 then 2 when p>=50 then 1 else 0 end
    from (select coalesce(sum(points),0)::int p from public.mission_completions where user_id=auth.uid()) s;
end $$;
```

Add a separate `set_journal_sharing(entry_id, share boolean)` RPC. It may only change the caller's note and only shares it with the currently assigned leader. RLS lets users CRUD their own notes; leaders read only notes explicitly shared by their assigned young users; admins have no blanket journal access.

Add `next_mission_on date` to `user_plans` and an owner-only `reschedule_next_mission(target_date)` RPC that accepts dates from today through seven days ahead. Replanning changes only the next recommendation date; it never deletes a completion, point or plant stage.

- [ ] **Step 4: Implement the daily loop**

The home screen shows today's single primary mission and plant. `MissionCard` offers “Completar misión”, “Hoy necesito algo breve” and, after a missed day, “Reprogramar”. The recovery version takes roughly two minutes and awards fewer points without shame language. `/camino` shows five weekly missions and two spaces labeled “Día flexible”; missed days do not display a red failure state.

Submit completion, await the RPC response, then update points and plant. On network failure show “No pudimos guardar todavía” and keep the completion button available; never show unconfirmed rewards.

- [ ] **Step 5: Verify**

Run: `npm --prefix raices run test:db`

Run: `npm --prefix raices run test:e2e -- mission.spec.ts`

Expected: duplicate submissions award once; recovery works; the plant never regresses; private and shared journal policies pass.

- [ ] **Step 6: Commit**

```powershell
git add raices/supabase/migrations/0003_progress_and_journal.sql raices/supabase/tests/database/0003_progress_rls.test.sql raices/src/components/plant.tsx raices/src/components/mission-card.tsx 'raices/src/app/(app)' raices/tests/e2e/mission.spec.ts
git commit -m "feat(raices): completar ciclo de crecimiento"
```

---

### Task 6: Add leader accompaniment and privacy-safe collective metrics

**Files:**
- Create: `raices/supabase/migrations/0004_accompaniment_and_metrics.sql`
- Test: `raices/supabase/tests/database/0004_accompaniment.test.sql`
- Create: `raices/src/app/(app)/mas/page.tsx`
- Create: `raices/src/app/admin/page.tsx`
- Test: `raices/tests/e2e/leader.spec.ts`

**Interfaces:**
- Consumes: leader assignments, mission completion timestamps and explicitly shared notes.
- Produces: non-diagnostic support alerts, leader view, admin overview and collective metrics with a five-user privacy threshold.

- [ ] **Step 1: Write failing database assertions**

Assert that an alert is created after three expected mission days without activity, a leader sees only assigned alerts/shared notes, admins cannot read private notes, and metrics return no counts when fewer than five young users are active.

- [ ] **Step 2: Confirm failure**

Run: `npm --prefix raices run test:db`

- [ ] **Step 3: Implement the database boundary**

Create `accompaniment_alerts(user_id, leader_id, reason, status, created_at, resolved_at)` and an idempotent daily `refresh_accompaniment_alerts()` SQL function. Reasons are limited to `no_activity_3_days` and `requested_help`; do not infer emotions or diagnoses.

Create `collective_metrics()` returning:

```sql
table(active_users integer, missions_completed integer, community_stage integer, hidden_for_privacy boolean)
```

When `active_users < 5`, return zeroed counts and `hidden_for_privacy = true`. Otherwise aggregate without names or user IDs. Schedule `refresh_accompaniment_alerts()` daily using Supabase Cron.

- [ ] **Step 4: Implement role-specific views**

Leaders see assigned names, activity recency, open alerts and only shared journal notes. They may resolve an alert after accompanying the person through the channels the group already uses; do not build chat or store new contact data. Admins see assignments, alerts and aggregate operations, never private journal bodies.

- [ ] **Step 5: Verify and commit**

Run: `npm --prefix raices run test:db && npm --prefix raices run test:e2e -- leader.spec.ts`

```powershell
git add raices/supabase/migrations/0004_accompaniment_and_metrics.sql raices/supabase/tests/database/0004_accompaniment.test.sql 'raices/src/app/(app)/mas/page.tsx' raices/src/app/admin/page.tsx raices/tests/e2e/leader.spec.ts
git commit -m "feat(raices): sumar acompañamiento seguro"
```

**Gate A acceptance:** one young user can register, finish onboarding, choose full or recovery missions, grow a non-regressive plant, keep/share a note, and trigger an alert visible only to the assigned leader.

---

### Task 7: Build the post-it prayer wall

**Files:**
- Create: `raices/supabase/migrations/0005_prayer_wall.sql`
- Test: `raices/supabase/tests/database/0005_prayer_privacy.test.sql`
- Create: `raices/src/lib/validation/prayer.ts`
- Create: `raices/src/components/prayer-wall.tsx`
- Create: `raices/src/app/(app)/oracion/page.tsx`
- Create: `raices/src/app/admin/oracion/page.tsx`
- Test: `raices/tests/e2e/prayer.spec.ts`

**Interfaces:**
- Consumes: authenticated identity and chosen visibility.
- Produces: safe prayer cards, “Oré por esto”, answered state and moderation reports.

- [ ] **Step 1: Write the failing privacy test**

Cover all three visibility choices: `network_named`, `network_anonymous`, `leaders_only`. Assert that the safe wall function never returns `user_id` or an author for anonymous requests, young users cannot see leader-only requests, and owners can mark only their own request answered.

- [ ] **Step 2: Confirm failure**

Run: `npm --prefix raices run test:db`

- [ ] **Step 3: Implement tables and safe RPC output**

Create `prayer_requests`, `prayer_supports` with unique `(request_id,user_id)`, and `prayer_reports`. Do not grant authenticated users general `select` on raw requests. Expose only a fixed-shape `get_prayer_wall()` security-definer RPC:

```sql
table(id uuid, author_name text, body text, status text, support_count integer, supported_by_me boolean, created_at timestamptz)
```

Its `author_name` is populated only for `network_named`; staff may also receive leader-only rows, still without leaking anonymous authors to ordinary wall consumers. Limit bodies to 500 characters and reports to one per user/request.

Replace `collective_metrics()` in this migration so its safe aggregate also includes `prayers_supported`; preserve the five-active-user threshold before returning any count.

- [ ] **Step 4: Implement the post-it interface**

Use CSS grid, rotated cards capped at subtle angles, sufficient contrast and an unrotated reduced-motion mode. The composer requires one explicit visibility radio choice. Cards expose only “Oré por esto”, count, owner-only “Respondida” and “Reportar”. The admin moderation page lists reports and can hide a request with a recorded reason; it never reveals the author of an anonymous network post. Do not add comments, reactions or direct messages.

- [ ] **Step 5: Verify and commit**

Run: `npm --prefix raices run test:db && npm --prefix raices run test:e2e -- prayer.spec.ts`

```powershell
git add raices/supabase/migrations/0005_prayer_wall.sql raices/supabase/tests/database/0005_prayer_privacy.test.sql raices/src/lib/validation/prayer.ts raices/src/components/prayer-wall.tsx 'raices/src/app/(app)/oracion/page.tsx' raices/src/app/admin/oracion/page.tsx raices/tests/e2e/prayer.spec.ts
git commit -m "feat(raices): crear muro de oración"
```

---

### Task 8: Unlock cards, badges, comics and wallpapers

**Files:**
- Create: `raices/supabase/migrations/0006_rewards.sql`
- Test: `raices/supabase/tests/database/0006_rewards.test.sql`
- Modify: `raices/src/app/(app)/page.tsx`
- Create: `raices/src/app/(app)/colecciones/page.tsx`
- Create: `raices/src/app/(app)/mas/wallpapers/page.tsx`
- Test: `raices/tests/e2e/rewards.spec.ts`

**Interfaces:**
- Consumes: server-confirmed points and admin-published rewards.
- Produces: permanent unlocks and downloadable verse wallpapers.

- [ ] **Step 1: Write failing unlock tests**

Assert that a reward with threshold 0 is available at signup, thresholds unlock once when confirmed points cross them, unlocked rewards remain unlocked, and no points are spent.

- [ ] **Step 2: Confirm failure**

Run: `npm --prefix raices run test:db`

- [ ] **Step 3: Add rewards and integrate them into mission completion**

Create `rewards(type card|badge|wallpaper|comic, title, body, asset_path, required_points, status)` and `user_rewards` with primary key `(user_id,reward_id)`. Extend `complete_mission()` to insert every newly eligible reward in the same transaction and return the newly unlocked IDs. Points are cumulative evidence of participation, not a balance.

- [ ] **Step 4: Build collections**

`/colecciones` filters cards, badges and “Verdad en dibujo”. Inicio highlights one unlocked active card below the primary mission. Locked items show the unlock condition without moral judgment. `/mas/wallpapers` uses ordinary download links; some published wallpapers have `required_points = 0`. Do not attempt automatic lock-screen changes from the PWA.

- [ ] **Step 5: Verify and commit**

Run: `npm --prefix raices run test:db && npm --prefix raices run test:e2e -- rewards.spec.ts`

```powershell
git add raices/supabase/migrations/0006_rewards.sql raices/supabase/tests/database/0006_rewards.test.sql 'raices/src/app/(app)/page.tsx' 'raices/src/app/(app)/colecciones/page.tsx' 'raices/src/app/(app)/mas/wallpapers/page.tsx' raices/tests/e2e/rewards.spec.ts
git commit -m "feat(raices): desbloquear colecciones"
```

---

### Task 9: Add the PDF library and optional adaptive reading

**Files:**
- Create: `raices/supabase/migrations/0007_library.sql`
- Test: `raices/supabase/tests/database/0007_library.test.sql`
- Create: `raices/supabase/functions/process-books/index.ts`
- Create: `raices/src/components/book-reader.tsx`
- Create: `raices/src/app/(app)/biblioteca/page.tsx`
- Create: `raices/src/app/(app)/biblioteca/[bookId]/page.tsx`
- Create: `raices/src/app/admin/biblioteca/page.tsx`
- Test: `raices/tests/unit/book-reader.test.tsx`
- Test: `raices/tests/e2e/library.spec.ts`

**Interfaces:**
- Consumes: admin-uploaded PDF and optional Adobe credentials.
- Produces: private signed original viewer, adaptive HTML view, bookmark and graceful fallback.

- [ ] **Step 1: Write the failing reader test**

```tsx
it('falls back to the original PDF when adaptive extraction is unavailable', () => {
  render(<BookReader book={{ id:'b', pdfUrl:'/signed.pdf', adaptiveStatus:'failed', adaptivePages:null }} />)
  expect(screen.getByTitle('Lector PDF')).toHaveAttribute('src', '/signed.pdf')
  expect(screen.queryByRole('button', { name: 'Vista adaptable' })).not.toBeInTheDocument()
})
```

- [ ] **Step 2: Confirm failure**

Run: `npm --prefix raices test -- book-reader.test.tsx`

- [ ] **Step 3: Add library persistence and storage policies**

Create private Storage bucket `books`, `books(id,title,author,pdf_path,adaptive_status,adobe_job_id,adaptive_json_path,status)` and `book_progress(user_id,book_id,page,location,updated_at)`. Only admins upload/change books. Authenticated users receive short-lived signed URLs only for published books and manage only their own progress.

- [ ] **Step 4: Process PDF extraction without a new server**

Schedule `process-books` every minute. For a `pending` book it starts Adobe PDF Extract and stores the job ID; for `processing` it polls; when complete it stores normalized page/block JSON in private Storage and marks `ready`. It validates MIME `application/pdf`, a 25 MB limit and Adobe response shape. A failed extraction marks `failed` but leaves the original published PDF usable.

- [ ] **Step 5: Implement both reading modes**

Original mode uses the browser PDF viewer in an iframe. Adaptive mode renders headings, paragraphs and images from normalized JSON with font-size controls. A page-like option uses CSS `scroll-snap-type` and `scroll-snap-align`; do not add a flipbook dependency. Save page/location after a one-second debounce.

- [ ] **Step 6: Verify and commit**

Run: `npm --prefix raices test -- book-reader.test.tsx`

Run: `npm --prefix raices run test:db`

Run: `npm --prefix raices run test:e2e -- library.spec.ts`

Expected: original, adaptive and fallback paths pass; unauthorized upload and cross-user progress access fail.

```powershell
git add raices/supabase/migrations/0007_library.sql raices/supabase/tests/database/0007_library.test.sql raices/supabase/functions/process-books raices/src/components/book-reader.tsx 'raices/src/app/(app)/biblioteca' raices/src/app/admin/biblioteca raices/tests/unit/book-reader.test.tsx raices/tests/e2e/library.spec.ts
git commit -m "feat(raices): agregar biblioteca adaptable"
```

---

### Task 10: Add opt-in reminders and conservative offline support

**Files:**
- Create: `raices/supabase/migrations/0008_push.sql`
- Test: `raices/supabase/tests/database/0008_push.test.sql`
- Create: `raices/supabase/functions/send-reminders/index.ts`
- Create: `raices/public/sw.js`
- Create: `raices/public/offline.html`
- Create: `raices/src/components/push-opt-in.tsx`
- Create: `raices/src/app/(app)/mas/notificaciones/page.tsx`
- Test: `raices/tests/e2e/pwa.spec.ts`

**Interfaces:**
- Consumes: explicit browser permission, reminder time/timezone and VAPID secrets.
- Produces: one daily reminder per user/device and safe offline fallback.

- [ ] **Step 1: Write failing database tests**

Assert that subscriptions belong to one user, endpoints are unique, a user cannot inspect another endpoint, and `(user_id, local_date, kind)` prevents duplicate reminder delivery.

- [ ] **Step 2: Confirm failure**

Run: `npm --prefix raices run test:db`

- [ ] **Step 3: Add subscriptions and delivery idempotency**

Create `push_subscriptions` and `notification_deliveries`. Store endpoint and keys server-side under RLS. `send-reminders` runs every 15 minutes, selects users whose local reminder time falls in the current window, claims a delivery row first, then sends through `npm:web-push`. On failure it records the error; expired endpoints are deleted. Store VAPID secrets in Supabase Secrets/Vault.

- [ ] **Step 4: Register the native service worker**

Ask permission only after the user presses “Activar recordatorios”. Cache versioned public shell assets and `offline.html`; use network-first for authenticated pages and never cache Supabase API/auth responses. A notification click opens today's mission. If permission or delivery fails, the mission remains available normally.

- [ ] **Step 5: Verify and commit**

Run: `npm --prefix raices run test:db && npm --prefix raices run test:e2e -- pwa.spec.ts`

Expected: manifest is installable, permission is user-initiated, duplicate sends are blocked and offline navigation shows the neutral fallback.

```powershell
git add raices/supabase/migrations/0008_push.sql raices/supabase/tests/database/0008_push.test.sql raices/supabase/functions/send-reminders raices/public/sw.js raices/public/offline.html raices/src/components/push-opt-in.tsx 'raices/src/app/(app)/mas/notificaciones/page.tsx' raices/tests/e2e/pwa.spec.ts
git commit -m "feat(raices): activar recordatorios PWA"
```

**Gate B acceptance:** prayer privacy, permanent unlocks, free wallpapers, original/adaptive books and opt-in reminders work without adding chat, rankings, automatic lock-screen access or a second backend.

---

### Task 11: Import the existing corpus and approve one editorial profile

**Files:**
- Create: `raices/supabase/migrations/0009_editorial.sql`
- Test: `raices/supabase/tests/database/0009_editorial.test.sql`
- Create: `raices/scripts/import-corpus.mjs`
- Create: `raices/supabase/functions/_shared/admin.ts`
- Create: `raices/supabase/functions/_shared/http.ts`
- Create: `raices/supabase/functions/_shared/openai.ts`
- Create: `raices/supabase/functions/generate-editorial-profile/index.ts`
- Create: `raices/src/app/admin/contenido/page.tsx`
- Test: `raices/tests/integration/editorial-profile.test.ts`

**Interfaces:**
- Consumes: existing `.md`, `.txt` and `.html` sermons/materials plus admin identity.
- Produces: immutable source records and exactly one admin-approved doctrinal/editorial profile.

- [ ] **Step 1: Write failing authorization and lifecycle tests**

Assert that only admins see corpus/profile rows, a generated profile starts `draft`, generation cannot publish it, and only an admin may move it to `approved`.

- [ ] **Step 2: Confirm failure**

Run: `npm --prefix raices run test:db`

- [ ] **Step 3: Add the editorial lifecycle**

Create `corpus_documents(id,title,source_path,content,sha256,created_at)`, `editorial_profiles(id,status,summary,doctrinal_boundaries,tone_rules,source_ids,approved_by,approved_at)` and `ai_runs(id,kind,status,model,input_chars,output_json,error,created_by,created_at)`. Enforce one approved profile with a partial unique index, and make profile generation refuse a new request after that first approval unless the existing profile is explicitly reopened by an admin migration.

Every Edge Function calls `requireAdmin(req)` using the caller JWT and `current_role()`. Limit generation to five admin calls per day initially. This is a cost/safety ceiling, not a general rate-limit framework.

- [ ] **Step 4: Import current materials without an indexing service**

`import-corpus.mjs` recursively accepts an explicit `--source` path, imports only `.md`, `.txt` and `.html`, strips script/style tags and basic markup, hashes content with Node `crypto`, and upserts by hash. It must refuse the workspace root and require `SUPABASE_SERVICE_ROLE_KEY` locally.

```powershell
node raices/scripts/import-corpus.mjs --source predicas
```

This intentionally skips DOCX/PDF extraction; use their Markdown/HTML counterparts or the admin library upload. Add broader parsers only if unique source material actually lacks a text version.

- [ ] **Step 5: Generate and approve the profile**

`generate-editorial-profile` sends bounded corpus excerpts to the OpenAI Responses API with `gpt-5.6-terra`, low reasoning and a strict JSON schema containing summary, doctrinal boundaries, recurring themes, tone, prohibited claims and pastoral cautions. Store only a draft. The admin page shows sources and every field, supports edit/regenerate, and requires an explicit “Aprobar perfil” action.

- [ ] **Step 6: Verify and commit**

Run: `npm --prefix raices run test:db`

Run: `npm --prefix raices test -- editorial-profile.test.ts`

Expected: a mocked structured response becomes a draft; malformed JSON produces a failed run and no profile; only an admin approves.

```powershell
git add raices/supabase/migrations/0009_editorial.sql raices/supabase/tests/database/0009_editorial.test.sql raices/scripts/import-corpus.mjs raices/supabase/functions/_shared raices/supabase/functions/generate-editorial-profile raices/src/app/admin/contenido raices/tests/integration/editorial-profile.test.ts
git commit -m "feat(raices): establecer perfil editorial"
```

---

### Task 12: Generate complete draft packages and publish atomically

**Files:**
- Create: `raices/supabase/migrations/0010_content_packages.sql`
- Test: `raices/supabase/tests/database/0010_publication.test.sql`
- Create: `raices/src/lib/validation/content.ts`
- Create: `raices/supabase/functions/generate-package/index.ts`
- Create: `raices/src/app/admin/contenido/[packageId]/page.tsx`
- Test: `raices/tests/integration/generate-package.test.ts`
- Test: `raices/tests/e2e/admin-review.spec.ts`

**Interfaces:**
- Consumes: approved editorial profile, optional later theme, no required initial admin idea.
- Produces: reviewable series/plan package and all-or-nothing publication into user-visible tables.

- [ ] **Step 1: Write the failing package contract test**

```ts
import { ContentPackage } from '@/lib/validation/content'

it('requires five missions and a recovery for every week', () => {
  const result = ContentPackage.safeParse({ title:'Esperanza', weeks:[{ missions:[] }] })
  expect(result.success).toBe(false)
})
```

The complete schema requires series title, a proposed publication calendar, plan title, summary, focus/intensity/time, weekly five missions, Bible references, reflections, action, recovery variant, guided-prayer script, reward cards, badges, comic briefs and wallpaper briefs.

- [ ] **Step 2: Confirm failure**

Run: `npm --prefix raices test -- generate-package.test.ts`

- [ ] **Step 3: Add draft/review state**

Create `content_packages(id,status draft|media_pending|ready|published|rejected,theme,content_json,version,generated_by_run,reviewed_by,published_at)` and `editorial_events(package_id,actor_id,action,before_json,after_json,created_at)`. The first generation request may omit `theme`; the prompt asks the model to choose a useful theme not duplicating published plans and place the series/plans in a proposed calendar. Later admins may supply a theme or change the calendar during review.

Use Structured Outputs and validate again server-side. A malformed/incomplete response marks `ai_runs.failed` and creates no package. Admin edits create a new version/event; regenerate never overwrites the reviewed version.

- [ ] **Step 4: Publish with one database transaction**

Implement `publish_content_package(package_id)` as an admin-only RPC. It revalidates `ready`, inserts the plan, five missions per week, cards, badges, scripts and visual briefs, then marks the package `published`. Any error rolls the entire transaction back. User queries only return published rows.

- [ ] **Step 5: Build the review screen**

Show the complete package in sections, source profile, validation errors and generation cost metadata. Actions: edit, regenerate section, generate media, reject, publish. Do not include automatic approval or scheduled publishing.

- [ ] **Step 6: Verify and commit**

Run: `npm --prefix raices test -- generate-package.test.ts`

Run: `npm --prefix raices run test:db`

Run: `npm --prefix raices run test:e2e -- admin-review.spec.ts`

Expected: no incomplete package appears to users; a forced insert error leaves zero partially published rows.

```powershell
git add raices/supabase/migrations/0010_content_packages.sql raices/supabase/tests/database/0010_publication.test.sql raices/src/lib/validation/content.ts raices/supabase/functions/generate-package 'raices/src/app/admin/contenido/[packageId]' raices/tests/integration/generate-package.test.ts raices/tests/e2e/admin-review.spec.ts
git commit -m "feat(raices): generar y revisar planes"
```

---

### Task 13: Generate reviewable audio and visual media

**Files:**
- Create: `raices/supabase/migrations/0011_media_assets.sql`
- Test: `raices/supabase/tests/database/0011_media.test.sql`
- Create: `raices/supabase/functions/generate-media/index.ts`
- Modify: `raices/src/app/admin/contenido/[packageId]/page.tsx`
- Modify: `raices/src/components/mission-card.tsx`
- Modify: `raices/src/app/(app)/oracion/page.tsx`
- Modify: `raices/src/app/(app)/colecciones/page.tsx`
- Test: `raices/tests/integration/generate-media.test.ts`

**Interfaces:**
- Consumes: admin-reviewed prayer scripts, comic briefs and wallpaper briefs.
- Produces: private draft media, admin preview/listening and published assets.

- [ ] **Step 1: Write failing lifecycle tests**

Assert that generated media is `draft`, ordinary users cannot read draft paths, audio failure leaves the prayer text valid, and publishing references only approved assets.

- [ ] **Step 2: Confirm failure**

Run: `npm --prefix raices run test:db`

- [ ] **Step 3: Generate one asset at a time**

Create `media_assets(package_id,kind audio|comic|wallpaper,status,storage_path,prompt,input_text,error,approved_by,approved_at)`. `generate-media` accepts exactly one package section per call, verifies admin role, then uses:

- `tts-1` on `/v1/audio/speech` for guided prayer audio.
- `gpt-image-2` on `/v1/images/generations` for comics and wallpapers.

Store bytes in a private `draft-media` bucket. Validate MIME, size and associated package. Do not run parallel bulk generation in the MVP; the admin should see cost and retry only the failed asset.

- [ ] **Step 4: Add human media approval**

The review page provides audio playback, image preview, approve, reject and regenerate. `publish_content_package` copies/references only approved assets into the published bucket. Audio is optional: if it fails, the reviewed text prayer remains publishable and visible. Published guided prayers are playable from both their mission and Oración. Comics/wallpapers are not published without an approved image.

- [ ] **Step 5: Verify and commit**

Run: `npm --prefix raices test -- generate-media.test.ts && npm --prefix raices run test:db`

```powershell
git add raices/supabase/migrations/0011_media_assets.sql raices/supabase/tests/database/0011_media.test.sql raices/supabase/functions/generate-media 'raices/src/app/admin/contenido/[packageId]/page.tsx' raices/src/components/mission-card.tsx 'raices/src/app/(app)/oracion/page.tsx' 'raices/src/app/(app)/colecciones/page.tsx' raices/tests/integration/generate-media.test.ts
git commit -m "feat(raices): revisar audio e imágenes IA"
```

**Gate C acceptance:** with no theme supplied, AI proposes a complete package from the approved profile; an admin can edit, listen, inspect and publish it; any generation or publication failure leaves users on the last approved content.

---

### Task 14: Close security, accessibility and end-to-end acceptance

**Files:**
- Modify: `raices/next.config.ts`
- Modify: `raices/src/app/globals.css`
- Create: `raices/playwright.config.ts`
- Create: `raices/tests/e2e/pilot-journey.spec.ts`
- Create: `raices/tests/e2e/privacy.spec.ts`
- Create: `raices/tests/e2e/accessibility.spec.ts`
- Create: `raices/docs/security-checklist.md`

**Interfaces:**
- Consumes: the complete application and three test accounts.
- Produces: launch-blocking evidence for roles, privacy, keyboard/screen-reader basics and critical journeys.

- [ ] **Step 1: Write acceptance tests before fixes**

The pilot journey covers admin publishing one plan, young signup/onboarding/recovery/journal/prayer, leader alert/shared-note access and admin aggregate view. Privacy tests attempt direct table/RPC access across users. Accessibility tests use `@axe-core/playwright`, keyboard navigation, accessible names, visible focus and reduced motion on every primary screen.

- [ ] **Step 2: Run and record failures**

Run: `npm --prefix raices run test:e2e -- pilot-journey.spec.ts privacy.spec.ts accessibility.spec.ts`

Expected: at least the missing headers/checklist assertions fail before hardening.

- [ ] **Step 3: Apply only evidenced hardening**

Add strict security headers in `next.config.ts`: Content-Security-Policy with browser `connect-src` limited to self and Supabase, `frame-src` for signed Supabase PDFs, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Permissions-Policy` and frame protection. OpenAI and Adobe remain server-only and therefore absent from browser CSP destinations. Validate every mutation with Zod or database constraints. Ensure admin actions use server-confirmed roles, signed URLs expire, uploads enforce type/size and logs omit prayer/journal bodies.

Fix all accessibility failures: semantic headings, labels, status announcements, focus restoration for dialogs, 44px targets, contrast and reduced motion. Do not add an accessibility component library.

- [ ] **Step 4: Run the complete quality gate**

```powershell
npm --prefix raices run lint
npm --prefix raices run typecheck
npm --prefix raices test
npm --prefix raices run test:db
npm --prefix raices run build
npm --prefix raices run test:e2e
```

Expected: every command exits 0. Any RLS or journal/privacy failure blocks launch.

- [ ] **Step 5: Commit**

```powershell
git add raices/next.config.ts raices/src/app/globals.css raices/playwright.config.ts raices/tests/e2e/pilot-journey.spec.ts raices/tests/e2e/privacy.spec.ts raices/tests/e2e/accessibility.spec.ts raices/docs/security-checklist.md
git commit -m "test(raices): cerrar seguridad y accesibilidad"
```

---

### Task 15: Deploy and run the two-person pilot

**Files:**
- Create: `raices/docs/deployment.md`
- Create: `raices/docs/pilot-runbook.md`
- Create: `raices/docs/go-live-checklist.md`
- Modify: `raices/.env.example`

**Interfaces:**
- Consumes: passing Gate D build, one leader, one young volunteer and a separate admin test account.
- Produces: Vercel preview/production, Supabase production configuration, one-week evidence and a go/no-go decision for 30+10 users.

- [ ] **Step 1: Document the exact production configuration**

`deployment.md` lists:

- Create/link one Supabase project; apply migrations and deploy five Edge Functions.
- Configure Google OAuth redirect URLs and disable unneeded providers.
- Create private/public buckets and verify policies.
- Store OpenAI, Adobe and VAPID secrets only in Supabase.
- Configure Supabase Cron for alerts, PDF jobs and reminders.
- Import the existing corpus, generate/approve the editorial profile and publish one reviewed plan.
- Deploy `raices/` to Vercel with only public Supabase URL/key.
- Configure custom domain later; it is not a pilot blocker.

Keep Railway absent. Note that Vercel/Supabase may stay on free allowances for this scale, while OpenAI/Adobe usage is metered and must have provider-side spend limits.

Extend `.env.example` with the exact server-only names `SUPABASE_SERVICE_ROLE_KEY`, `OPENAI_API_KEY`, `ADOBE_PDF_SERVICES_CLIENT_ID`, `ADOBE_PDF_SERVICES_CLIENT_SECRET`, `VAPID_PUBLIC_KEY`, `VAPID_PRIVATE_KEY` and `VAPID_SUBJECT`. Document that Vercel receives only the two `NEXT_PUBLIC_SUPABASE_*` values; the remaining values belong in the local import environment or Supabase Secrets/Vault.

- [ ] **Step 2: Create exactly three pilot accounts**

1. Admin test account owned by the leader for editorial/admin checks.
2. Leader account assigned to the volunteer.
3. Young volunteer account.

Do not share a single session between roles; test in separate browser profiles/incognito contexts.

- [ ] **Step 3: Run the seven-day protocol**

Daily capture only operational data already defined: login success, mission/recovery completion, save failures, reminder delivery, unclear screens, support alert usefulness and any privacy concern. Ask the volunteer a short qualitative question after days 2 and 7: “¿Qué te ayudó y qué te hizo sentir presión?”. Do not collect clinical or diagnostic responses.

- [ ] **Step 4: Apply go/no-go criteria**

Launch to 30 young users and 10 leaders only if:

- No role/RLS/privacy incident occurred.
- The volunteer could recover after a missed mission without losing plant progress.
- The leader received only assigned information.
- At least one full mission, one recovery, one prayer interaction and one reminder completed successfully.
- All errors degraded as specified: no partial publish, text survives audio failure, original PDF survives adaptive failure, mission survives notification failure, and points wait for server confirmation.

If privacy fails, stop and fix before launch. If only UX wording is unclear, fix the wording and repeat the affected day, not the whole pilot.

After a go decision, monitor the first public beta week daily with the same operational checklist, now adding device/browser variety and leader-assignment distribution. Treat privacy and data-loss defects as immediate launch blockers; batch minor visual issues for the next reviewed release.

- [ ] **Step 5: Final verification and commit**

Run: `npm --prefix raices run check && npm --prefix raices run test:e2e`

```powershell
git add raices/.env.example raices/docs/deployment.md raices/docs/pilot-runbook.md raices/docs/go-live-checklist.md
git commit -m "docs(raices): preparar piloto interno"
```

**Gate D acceptance:** the deployed PWA passes the three-account journey, the one-week pilot records no privacy blocker, and the go-live checklist explicitly authorizes—or stops—the 30+10 beta.

## Explicitly Deferred

- Native Android/iOS app and automatic lock-screen verse.
- Deep personal analysis until a qualified specialist defines its safeguards.
- Individual rankings, streak punishment, points marketplace or plant regression.
- Comments, public/private in-app chat and peer-to-peer messaging.
- Multiple AI providers, vector search, a queue service and Railway.
- DOCX-specific corpus extraction and elaborate page-turn physics.

Add any deferred item only after observed pilot evidence shows the current solution is insufficient.
