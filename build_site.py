"""Builds the Predawn marketing site (same structure as sunblush-site / udana-site)."""
import os, sys

OUT = sys.argv[1]
BASE = "https://jakeintech.github.io/predawn-site/"
APP_ID = "6834539845"
STORE = f"https://apps.apple.com/app/id{APP_ID}"
EMAIL = "info@jakeawilliams.com"
UPDATED = "November 16, 2026"

CSS = """:root{--bg:#0B0B12;--bg2:#15151F;--bg3:#1E1E2A;--label:#F5F5F7;--label2:#AEAEBA;--label3:#7C7C8A;--accent:#D6F45A;--onaccent:#0B0B12;--sep:rgba(255,255,255,.10);--golden:#FFB340;--blue:#7D7AFF;color-scheme:dark}
@media (prefers-color-scheme:light){:root{--bg:#F7F7F9;--bg2:#FFFFFF;--bg3:#EFEFF4;--label:#0B0B12;--label2:#4A4A55;--label3:#6E6E78;--accent:#566A00;--onaccent:#FFFFFF;--sep:rgba(0,0,0,.10);color-scheme:light}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--label);font:17px/1.55 -apple-system,BlinkMacSystemFont,"SF Pro Text","Helvetica Neue",Arial,sans-serif}
a{color:var(--accent)}a:focus-visible,button:focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:6px}
.skip{position:absolute;left:-999px;top:8px;background:var(--accent);color:var(--onaccent);padding:8px 14px;border-radius:999px;z-index:9}.skip:focus{left:16px}
.wrap{max-width:1080px;margin-left:auto;margin-right:auto;padding-left:20px;padding-right:20px}
.site-head{display:flex;align-items:center;justify-content:space-between;padding-top:18px;padding-bottom:18px}
.brand{display:flex;align-items:center;gap:10px;font:700 20px/1 ui-rounded,"SF Pro Rounded",-apple-system,sans-serif;color:var(--label);text-decoration:none}
.brand img{border-radius:8px}
.site-nav{display:flex;gap:20px;align-items:center}.site-nav a{color:var(--label2);text-decoration:none;font-weight:500}.site-nav a:hover{color:var(--label)}.site-nav a.btn{color:var(--onaccent);min-height:44px;padding:0 18px}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 24px;border-radius:999px;background:var(--accent);color:var(--onaccent);font-weight:600;text-decoration:none}
.btn.ghost{background:var(--bg3);color:var(--label)}
.hero{padding-top:56px;padding-bottom:40px;display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center}
.eyebrow{font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--label2)}
h1{font:800 clamp(40px,6vw,68px)/1.02 ui-rounded,"SF Pro Rounded",-apple-system,sans-serif;letter-spacing:-.02em;margin:12px 0 18px}
h2{font:700 clamp(28px,3.6vw,40px)/1.1 ui-rounded,"SF Pro Rounded",-apple-system,sans-serif;letter-spacing:-.01em;margin:0 0 12px}
h3{font-size:20px;margin:0 0 6px}
.lede{font-size:20px;color:var(--label2);max-width:34ch;margin:0 0 28px}
.cta{display:flex;gap:12px;flex-wrap:wrap;align-items:center}.note{color:var(--label3);font-size:15px}
.phone{width:100%;max-width:340px;justify-self:center;border-radius:44px;box-shadow:0 0 0 1px var(--sep),0 30px 80px rgba(0,0,0,.45)}
section{padding-top:56px;padding-bottom:56px}.section-head{max-width:620px;margin-bottom:28px}.section-head p{color:var(--label2);margin:0}
.features{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.card{background:var(--bg2);border-radius:26px;padding:22px;box-shadow:inset 0 0 0 1px var(--sep)}
.card p{color:var(--label2);margin:0}
.shots{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;align-items:start}
.shot figure{margin:0}.shot img{width:100%;border-radius:30px;box-shadow:0 0 0 1px var(--sep)}
.shot figcaption{margin-top:12px}.shot figcaption b{display:block}.shot figcaption span{color:var(--label2);font-size:15px}
.tools{columns:2;gap:28px;padding:0;margin:0;list-style:none}.tools li{break-inside:avoid;padding:8px 0;border-bottom:1px solid var(--sep)}
.pricing{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.price{font:700 34px/1.1 ui-rounded,"SF Pro Rounded",-apple-system,sans-serif;margin:8px 0}
.price small{font-size:16px;color:var(--label2);font-weight:500}
.card ul{margin:12px 0 0;padding-left:20px;color:var(--label2)}
.card.hi{box-shadow:inset 0 0 0 2px var(--accent)}
.privacy{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.legal{max-width:760px;padding:40px 20px 72px}.legal h1{font-size:44px}.legal h2{font-size:24px;margin-top:36px}
.legal p,.legal li{color:var(--label2)}.legal strong{color:var(--label)}
.updated{color:var(--label3)}
table{width:100%;border-collapse:collapse;font-size:15px;margin:16px 0}th,td{text-align:left;vertical-align:top;padding:10px 8px;border-bottom:1px solid var(--sep)}th{color:var(--label);font-size:13px;text-transform:uppercase;letter-spacing:.05em}td{color:var(--label2)}
.faq dt{font-weight:600;margin-top:18px}.faq dd{margin:6px 0 0;color:var(--label2)}
.site-foot{border-top:1px solid var(--sep);padding:28px 20px 48px;color:var(--label3);font-size:14px}
.site-foot nav{display:flex;gap:18px;flex-wrap:wrap;margin-bottom:10px}.site-foot a{color:var(--label2);text-decoration:none}
@media (max-width:560px){.site-nav a.btn{display:none}.site-nav{gap:16px}.lede{font-size:18px}}
@media (max-width:820px){.hero{grid-template-columns:1fr;padding-top:24px}.features,.shots,.pricing{grid-template-columns:1fr}.privacy{grid-template-columns:1fr 1fr}.tools{columns:1}.phone{max-width:280px}}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
"""

def page(title, desc, path, body, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<meta name="theme-color" content="#0B0B12">
<link rel="canonical" href="{BASE}{path}">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Predawn">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:image" content="{BASE}assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE}assets/og.png">
<link rel="stylesheet" href="assets/site.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="wrap site-head">
  <a class="brand" href="./" aria-label="Predawn home"><img src="assets/icon-192.png" alt="" width="30" height="30">Predawn</a>
  <nav class="site-nav" aria-label="Site">
    <a href="./#pricing">Pricing</a>
    <a href="support.html">Support</a>
    <a class="btn" href="{STORE}">Get the app</a>
  </nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-foot wrap">
  <nav aria-label="Footer"><a href="./">Home</a><a href="support.html">Support</a><a href="privacy-policy.html">Privacy Policy</a><a href="terms-of-service.html">Terms of Use</a><a href="mailto:{EMAIL}">Contact</a></nav>
  <p>&copy; 2026 Jake Williams. Apple, iPhone, iPad and App Store are trademarks of Apple Inc. Map data from Apple Maps; forecasts from Apple Weather; tide predictions from NOAA; building heights &copy; OpenStreetMap contributors (ODbL) and from Wikidata (CC0). Terrain: Copernicus DEM, &copy; DLR e.V. 2010&ndash;2014 and &copy; Airbus Defence and Space GmbH 2014&ndash;2018, provided under COPERNICUS by the European Union and ESA.</p>
</footer>
</body>
</html>
"""

LD = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"Predawn: Sun & Moon Planner","operatingSystem":"iOS 26 or later","applicationCategory":"PhotographyApplication","description":"Pick a landmark, choose the sun or the moon, and Predawn finds the dates it lines up, where to stand and the camera settings.","url":"{BASE}","downloadUrl":"{STORE}","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}},"author":{{"@type":"Person","name":"Jake Williams"}}}}
</script>
"""

SHOTS = [
    ("tonight", "Is tonight worth it?", "Moon, darkness and cloud in one answer, with every light band to the minute."),
    ("finddates", "Describe the shot", "Full moon behind the lighthouse? Say so, and get the dates it lines up."),
    ("planner", "Where to stand", "Sun and moon lines on the map, your lens, your minute, to the foot."),
    ("scout", "See it before you go", "A 3D view from your spot with the light at the minute you chose."),
    ("rednight", "Red night", "Keeps your eyes dark-adapted when the shoot starts."),
    ("offline", "Ready with no signal", "Timeline, line of sight and alerts, saved with the plan."),
]
TOOLS = ["Long exposure (ND filters)", "Sharp stars (NPF and 500 rule)", "Star trails", "Time-lapse", "Exposure match",
         "Sun and moon exposure", "Hyperfocal distance", "Depth of field", "Focus stacking", "Field of view",
         "Panorama", "Subject size", "Lens match", "Shadow length", "Polar alignment"]

shots_html = "\n".join(f"""  <div class="shot"><figure><img src="assets/shot-{s}.webp" alt="Predawn {t.lower()} screen" width="440" height="956" loading="lazy"><figcaption><b>{t}</b><span>{d}</span></figcaption></figure></div>""" for s, t, d in SHOTS)
tools_html = "\n".join(f"    <li>{t}</li>" for t in TOOLS)

INDEX = f"""<section class="wrap hero">
  <div>
    <span class="eyebrow">Sun &amp; moon photo planner for iPhone</span>
    <h1>Know the minute.</h1>
    <p class="lede">Pick a landmark, choose the sun or the moon, and Predawn finds the dates it lines up, where to stand and what to dial in. Then it checks the sky and gets you there on time.</p>
    <div class="cta"><a class="btn" href="{STORE}">Download on the App Store</a><span class="note">Free to start. No account.</span></div>
  </div>
  <img class="phone" src="assets/shot-planner.webp" alt="Predawn's plan map: the full moon lined up behind Portland Head Light at 4:23 PM, seen from Ship Cove" width="440" height="956">
</section>

<section class="wrap" aria-labelledby="how">
  <div class="section-head"><h2 id="how">Plan the picture, not the paperwork</h2><p>Most planners give you a map full of lines and leave the maths to you. Predawn starts with the answer.</p></div>
  <div class="features">
    <div class="card"><h3>An answer for tonight</h3><p>Go, Check or No for the night sky, with the reason: the moon, how long it's truly dark, and the cloud forecast hour by hour.</p></div>
    <div class="card"><h3>Dates from a sentence</h3><p>"Full moon rising behind the lighthouse, near sunset." Predawn searches the year and lists every match, best light first, with how far to step left or right.</p></div>
    <div class="card"><h3>Will anything block it?</h3><p>Line of sight checks the ground between you and the horizon and tells you when the moon clears the rocks or the sun clears the ridge.</p></div>
    <div class="card"><h3>See it from anywhere</h3><p>Scout shows a 3D view from your spot with the light at the minute you chose. On site, the camera view shows where the sun and moon will rise.</p></div>
    <div class="card"><h3>Gets you there on time</h3><p>Leave-now and wake alarms from your drive and walk, a countdown in the Dynamic Island, and a forecast re-check 48 and 3 hours before.</p></div>
    <div class="card"><h3>Built for the dark</h3><p>Red night keeps your eyes adapted. Big targets for gloved hands. Saved plans keep working without signal.</p></div>
  </div>
</section>

<section class="wrap" aria-labelledby="look">
  <div class="section-head"><h2 id="look">A look inside</h2><p>Real screens from the app, planning a full moon behind Portland Head Light, Maine.</p></div>
  <div class="shots">
{shots_html}
  </div>
</section>

<section class="wrap" aria-labelledby="tools">
  <div class="section-head"><h2 id="tools">Every tool you reach for</h2><p>Set your camera and lens once. Every calculator starts from your gear and your plan.</p></div>
  <ul class="tools">
{tools_html}
  </ul>
</section>

<section class="wrap" id="pricing" aria-labelledby="price-h">
  <div class="section-head"><h2 id="price-h">Free to start</h2><p>Tonight, planning, Find dates, the camera view and most tools are free. Pro is for the night shooters and the obsessive planners.</p></div>
  <div class="pricing">
    <div class="card"><h3>Free</h3><div class="price">$0</div><ul><li>Tonight's verdict and every light band</li><li>Plan map with sun and moon lines, line of sight and clouds</li><li>Find dates and matches</li><li>Camera view and Scout</li><li>Most calculators</li></ul></div>
    <div class="card hi"><h3>Pro, yearly</h3><div class="price">$19.99 <small>/ year</small></div><ul><li>1-week free trial for new subscribers</li><li>Milky Way, shadow and tide layers</li><li>Forecast alerts and cloud by height</li><li>More than one Field pack</li><li>NOAA tides, polar alignment, star trails, time-lapse</li><li>Apple Watch app</li></ul></div>
    <div class="card"><h3>Pro, once</h3><div class="price">$39.99</div><ul><li>Everything in Pro</li><li>One purchase, no subscription</li><li>Yours to keep</li></ul></div>
  </div>
  <p class="note" style="margin-top:16px">US prices; they may differ in your country. The yearly plan renews automatically unless cancelled at least 24 hours before it ends. Manage it in your Apple Account settings.</p>
</section>

<section class="wrap" aria-labelledby="priv">
  <div class="section-head"><h2 id="priv">Private by default</h2></div>
  <div class="privacy">
    <div class="card"><h3>No account</h3><p>Nothing to sign up for.</p></div>
    <div class="card"><h3>On your iPhone</h3><p>Plans, places and gear stay on the device.</p></div>
    <div class="card"><h3>No tracking</h3><p>No ads, no analytics, no third-party code.</p></div>
    <div class="card"><h3>No server of ours</h3><p>Forecasts from Apple Weather, maps from Apple Maps, terrain from public Copernicus files. Only Apple sees your exact spot.</p></div>
  </div>
  <p class="note" style="margin-top:16px"><a href="privacy-policy.html">Read the privacy policy</a></p>
</section>

<section class="wrap" style="text-align:center">
  <h2>Know the minute.</h2>
  <p class="note">Predawn for iPhone. Requires iOS 26 or later.</p>
  <a class="btn" href="{STORE}">Download on the App Store</a>
</section>
"""

PRIVACY = f"""<article class="legal">
<h1>Privacy Policy</h1>
<p class="updated">Last updated {UPDATED}</p>
<h2>The short version</h2>
<ul>
<li>Predawn has no accounts, no ads and no analytics or tracking software.</li>
<li>Your plans, places, gear and photos stay on your device.</li>
<li>Your location is used on your device. Its coordinates are sent to Apple to fetch the weather forecast, maps and place search. They are not sent to us.</li>
<li>We do not run a server that receives your data, and we do not sell or share personal information.</li>
</ul>
<h2>1. Who we are</h2>
<p>Predawn is a sun and moon photo planner for iPhone and iPad made by Jake Williams ("we", "us"). This policy explains what information the app handles, where it goes and the choices you have. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>2. What the app handles</h2>
<table>
<thead><tr><th>Information</th><th>What it is used for</th><th>Where it goes</th></tr></thead>
<tbody>
<tr><td>Precise location</td><td>Sun and moon times and positions where you are, tonight's verdict, and the forecast.</td><td>Used on your device. Coordinates are sent to Apple Weather for the forecast and to Apple Maps for maps and place names. Not sent to us.</td></tr>
<tr><td>Terrain</td><td>Ground heights for line of sight and for the spot and landmark you plan with.</td><td>Downloaded from the public Copernicus DEM files on Amazon Web Services. Requests name only the one-degree map square (about 100 km across), never your exact position, and carry no identifier. The files are kept on your device.</td></tr>
<tr><td>Landmark heights</td><td>How tall a building or landmark you plan with is, so the angles are right.</td><td>When a landmark you chose has no height yet, its coordinates are sent to OpenStreetMap (Overpass) and, if that finds nothing, to Wikidata. Only the landmark&rsquo;s position is sent: not its name, not your location, and no identifier. The height is kept on your device.</td></tr>
<tr><td>Tides (Pro)</td><td>Tide heights for the place you plan at, on US coasts.</td><td>NOAA's station list is downloaded and the nearest station is chosen on your device. NOAA is asked only for that station's number and the dates; never your location. Predictions are kept on your device.</td></tr>
<tr><td>Plans, places and gear</td><td>Your saved shoots, spots, cameras, lenses and settings.</td><td>Stored on your device. Widgets read them through a shared container on the same device.</td></tr>
<tr><td>Camera (optional)</td><td>The camera view that shows where the sun and moon will be over the scene.</td><td>Shown live on your screen. Nothing is recorded or stored.</td></tr>
<tr><td>Photos (optional)</td><td>Attaching the photo you took to a plan.</td><td>Only the photo you pick, kept on your device.</td></tr>
<tr><td>Calendar (optional, add only)</td><td>Adding a shoot and its leave time to your calendar when you ask.</td><td>Written to your calendar on your device. Predawn cannot read your calendar.</td></tr>
<tr><td>Purchases</td><td>Unlocking Predawn Pro.</td><td>Handled by Apple. We do not receive your name, payment details or purchase history.</td></tr>
<tr><td>Crash reports</td><td>Fixing bugs.</td><td>Predawn sends none itself. If you have chosen to share analytics with app developers in iOS Settings, Apple may send us crash reports that do not identify you.</td></tr>
</tbody>
</table>
<p>On the App Store, Predawn's privacy label lists one item, Precise Location, used for App Functionality, not linked to you and not used for tracking. It is listed because forecast requests to Apple Weather include coordinates.</p>
<h2>3. Location</h2>
<p>With your permission, Predawn uses your location to work out tonight's light, the sun and the moon where you are, and to request the forecast for that spot. You can refuse or withdraw permission at any time in Settings &gt; Privacy &amp; Security &gt; Location Services &gt; Predawn. Without it you can still choose any place by searching or dropping a pin.</p>
<h2>4. Weather, maps, terrain, landmark heights and tides</h2>
<p>Forecasts come from Apple Weather (WeatherKit). Each request contains the coordinates of your location or a place you chose, and nothing that identifies you to us. Maps, place search, 3D views and Look Around use Apple Maps. Apple handles these requests under <a href="https://www.apple.com/legal/privacy/">its own privacy policy</a>. Tide predictions (Pro) come from NOAA's public tide service: Predawn downloads NOAA's list of stations, picks the nearest one on your device, and asks NOAA only for that station's number and the dates you are looking at, never your location. All sun and moon calculations, line of sight, terrain shadows and tonight's verdict are worked out on your device.</p>
<p>Hills and ridges come from Copernicus DEM, a free elevation model published by the European Union and ESA and hosted by Amazon Web Services. When you plan with a spot and a landmark, the app downloads the parts of the one-degree map squares they sit in. A request names the map square (for example "N39 W105") and a byte range, nothing that identifies you or your exact position; as with any download, Amazon sees the network address the request comes from. Amazon handles these requests under <a href="https://aws.amazon.com/privacy/">its own privacy notice</a>. Downloaded terrain is kept on your device (not backed up) so plans work without signal.</p>
<p>Landmark heights come from OpenStreetMap and Wikidata. When you make a building or landmark the subject of a plan and Predawn doesn&rsquo;t know its height, it asks the public OpenStreetMap Overpass service (overpass-api.de) for buildings within about 150&nbsp;m of the landmark&rsquo;s coordinates, and if none has a height, asks the Wikidata Query Service (query.wikidata.org, run by the Wikimedia Foundation) the same about tagged heights nearby. The request contains only those coordinates and the app&rsquo;s name and version; picking the right building happens on your device. Each landmark is looked up once, and a height you type yourself is never replaced. As with any download, these services see the network address the request comes from and handle it under their own privacy policies.</p>
<h2>5. Notifications and alarms</h2>
<p>Forecast re-checks, leave-now reminders and wake alarms are scheduled on your device. No push notification server is involved, and we do not know whether an alert was delivered or opened.</p>
<h2>6. Purchases</h2>
<p>Predawn Pro is sold by Apple as a yearly subscription or a one-time purchase. Apple processes the payment and tells the app on your device whether Pro is unlocked. We do not see your card number, billing address or Apple Account.</p>
<h2>7. What we do not do</h2>
<ul><li>No accounts or sign-in.</li><li>No advertising, and no advertising identifier.</li><li>No third-party analytics, tracking or crash-reporting software.</li><li>No sale or sharing of personal information.</li></ul>
<h2>8. Keeping and deleting your data</h2>
<p>Your plans, places, gear and settings stay on your device until you delete them. You can delete any plan in the app. Deleting Predawn removes everything it stored. Because we hold none of your data, there is nothing for us to delete on our side.</p>
<h2>9. Children</h2>
<p>Predawn is rated 4+ and is not directed at children. We do not knowingly collect personal information from children under 13. If you believe a child has sent us personal information by email, contact us and we will delete it.</p>
<h2>10. Your rights</h2>
<p>Depending on where you live, laws such as the GDPR or the CCPA give you rights to access, correct, delete or restrict the use of your personal data. Because your data is stored on your own device, you can do these things directly in the app. If you have a request we can help with, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>11. Security</h2>
<p>Predawn relies on the protections built into iOS: its data sits inside the app's sandbox, protected by your passcode and the device's encryption, and every network request uses HTTPS.</p>
<h2>12. Changes</h2>
<p>If this policy changes, we will update the date at the top of this page. For a significant change we will also say so in the app.</p>
<h2>13. Contact</h2>
<p>Jake Williams<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
</article>
"""

TERMS = f"""<article class="legal">
<h1>Terms of Use</h1>
<p class="updated">Last updated {UPDATED}</p>
<h2>1. Agreement</h2>
<p>These terms cover your use of the Predawn app for iPhone and iPad, provided by Jake Williams ("we", "us"). By downloading or using Predawn you agree to them. If you do not agree, do not use the app. Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">standard end user license agreement</a> also applies.</p>
<h2>2. What Predawn does</h2>
<p>Predawn is a sun and moon photo planner. It includes:</p>
<ul>
<li><strong>Tonight.</strong> Light times, the moon and a verdict for the night sky based on Apple Weather data.</li>
<li><strong>Planning.</strong> Sun and moon positions on a map, Find dates for alignments with a subject, line of sight, a 3D scout view and a camera view.</li>
<li><strong>Saved plans.</strong> Timelines, pack lists, alerts and alarms, kept on your device.</li>
<li><strong>Tools.</strong> Photography calculators and polar alignment.</li>
<li><strong>Widgets and more.</strong> Home Screen and Lock Screen widgets, a Live Activity, Siri and Control Center controls.</li>
</ul>
<h2>3. Who can use it</h2>
<p>Predawn is rated 4+ on the App Store. You must be at least 13 to use it. If you are under the age of majority where you live, you need a parent's or guardian's permission.</p>
<h2>4. License</h2>
<p>We grant you a personal, non-exclusive, non-transferable, revocable license to use Predawn on Apple devices you own or control, as allowed by the App Store's usage rules. You may not copy, modify, sell, lease or reverse engineer the app, except where the law allows it.</p>
<h2>5. Predawn Pro</h2>
<p>Predawn is free to download and use. Predawn Pro unlocks extra features and is offered in two ways:</p>
<ul>
<li><strong>Yearly:</strong> $19.99 per year, renewing each year until cancelled, with a one-week free trial for eligible new subscribers.</li>
<li><strong>Once:</strong> $39.99. It does not renew and unlocks Pro for as long as the app is offered.</li>
</ul>
<p>Prices are for the United States and may differ elsewhere. Payment is charged to your Apple Account when you confirm the purchase. The subscription renews automatically unless you turn off auto-renew at least 24 hours before the end of the current period. Manage or cancel it in your App Store account settings. If you start a free trial and do not cancel before it ends, it becomes a paid subscription. Any unused part of a free trial is forfeited when you buy a subscription. Refunds are handled by Apple under its policies.</p>
<h2>6. Acceptable use and safety</h2>
<p>You agree not to use Predawn to break the law, to trespass, to enter closed or restricted areas, or to interfere with the app or the services it relies on. Places in the app, including the standing spots it suggests, may be private property, closed at certain hours, or dangerous: cliffs, tides, ice, wildlife, traffic and darkness. Check access rules and conditions yourself, and decide for yourself whether a place is safe.</p>
<h2>7. Calculations and forecasts are estimates</h2>
<p>Sun and moon positions are calculated to a high standard, but results depend on your device's location, the elevation data available and the settings you choose. Line of sight is an estimate from the terrain data available and the heights you enter. Forecasts come from Apple Weather and can be incomplete, delayed or wrong. Tide figures marked as sample data are illustrations, not predictions.</p>
<p>Do not rely on Predawn for navigation, safety, tide timing or any activity where a wrong time, place or forecast could cause harm.</p>
<h2>8. No warranty</h2>
<p>Predawn is provided "as is" and "as available", without warranties of any kind, express or implied, including merchantability, fitness for a particular purpose and non-infringement, to the extent the law allows.</p>
<h2>9. Limit of liability</h2>
<p>To the fullest extent the law allows, we are not liable for indirect, incidental, special, consequential or punitive damages, or for lost profits, data or goodwill, arising from your use of Predawn. Our total liability for any claim will not exceed the greater of what you paid us in the twelve months before the claim or twenty US dollars ($20).</p>
<h2>10. Ending these terms</h2>
<p>You can stop at any time by deleting the app. We may end or suspend your access if you seriously breach these terms or if we stop offering the app. Sections 7 to 9 and 12 continue to apply afterwards.</p>
<h2>11. Changes</h2>
<p>We may update these terms. If we do, we will change the date at the top of this page and, for a significant change, say so in the app. Using Predawn after a change means you accept the new terms.</p>
<h2>12. Governing law</h2>
<p>These terms are governed by the laws of the place where the developer lives, without regard to conflict-of-law rules. Disputes will be heard in the courts there, unless consumer law where you live gives you the right to bring a claim locally.</p>
<h2>13. Apple</h2>
<p>These terms are between you and us, not Apple. Apple is not responsible for Predawn or its content and has no obligation to provide support for it.</p>
<h2>14. Contact</h2>
<p>Jake Williams<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
</article>
"""

FAQ = [
 ("Getting started", [
  ("What does Predawn need to work?", "An iPhone or iPad on iOS 26 or later. Location helps for tonight's light where you are; without it, search for a place or drop a pin."),
  ("Do I need an account?", "No. There is nothing to sign up for. Your plans stay on your device."),
 ]),
 ("Tonight and the forecast", [
  ("What do Go, Check and No mean?", "They answer whether tonight is worth going out for the night sky. The score combines how clear the forecast is during full darkness, whether the moon is down or thin, and how long it is truly dark. Tap the verdict for the reasons and the cloud by hour."),
  ("It says the forecast didn't load.", "Forecasts come from Apple Weather and need a connection. Sun and moon times always work offline. Open the app again when you are back online."),
  ("Why do the times differ from another app by a minute?", "Predawn uses the standard definitions: sunrise and sunset when the top of the sun touches the horizon, and twilights by the sun's centre. Golden hour runs from 6° above to 4° below the horizon, blue hour from 4° to 6° below. Other apps choose other angles."),
 ]),
 ("Planning", [
  ("How do I line up the moon with a landmark?", "Tap Find dates. Choose the sun or the moon, rising or setting, the landmark you want it behind, and where you can stand. Predawn searches the next year and lists every match, best light first, with how far to step to centre it."),
  ("What does \"stand 35 ft to the right\" mean?", "On that date the moon reaches the landmark a little to one side. Move that far, sideways to the line between you and the landmark, and it sits dead centre."),
  ("How does line of sight work?", "It checks the ground between you and the horizon in the direction of the sun or moon and tells you the margin, and the minute it clears anything in the way. Terrain comes from Copernicus DEM, downloaded for the area you plan in and kept for use offline. If it can't load, Predawn says so and treats both ends as level ground; you can also enter the height of what's in front of you."),
  ("Does the camera view work everywhere?", "It needs a device with a camera and works best after a short calibration: point at the sun or moon to lock the compass. Without a camera, use Scout's 3D view instead."),
 ]),
 ("Alerts and the field", [
  ("Which alerts will I get?", "For each saved plan: a forecast re-check 48 and 3 hours before (it says if the outlook changed), a leave-now reminder based on drive and walk time, and an optional wake alarm. Change them in Settings > Alerts."),
  ("How do I turn on Red night?", "From Settings, the Control Center control, or let it turn on by itself after dark."),
  ("Will my plan work with no signal?", "Yes. Times, positions, line of sight and the timeline are saved with the plan. Maps you haven't viewed may not load offline."),
 ]),
 ("Predawn Pro", [
  ("What does Pro add?", "Milky Way core, terrain shadow and tide layers on the map, forecast alerts and cloud by height, more than one Field pack, NOAA tide predictions for US coasts, polar alignment, star trails, time-lapse and the Apple Watch app."),
  ("How do I restore a purchase?", "Open the Pro screen from Settings and tap Restore Purchases. Use the same Apple Account you bought with."),
  ("How do I cancel the yearly plan?", "In Settings > [your name] > Subscriptions on your iPhone, at least 24 hours before it renews."),
 ]),
]
faq_html = "\n".join(f"<h2>{sec}</h2>\n<dl class=\"faq\">" + "".join(f"<dt>{q}</dt><dd>{a}</dd>" for q, a in qs) + "</dl>" for sec, qs in FAQ)
SUPPORT = f"""<article class="legal">
<h1>Support</h1>
<p class="updated">Help with Predawn</p>
<h2>Get in touch</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a>. It helps to include your device, your iOS version, the place and date you were planning, and what you expected to happen. A person reads every message.</p>
{faq_html}
</article>
"""

os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
open(os.path.join(OUT, "assets/site.css"), "w").write(CSS)
files = {
 "index.html": page("Predawn: Sun & Moon Photo Planner for iPhone. Know the minute.", "Pick a landmark, choose the sun or the moon, and Predawn finds the dates it lines up, where to stand and the camera settings. Free on iPhone and iPad.", "", INDEX, LD),
 "privacy-policy.html": page("Predawn Privacy Policy", "How Predawn handles your information: no accounts, no tracking, everything on your device.", "privacy-policy.html", PRIVACY),
 "terms-of-service.html": page("Predawn Terms of Use", "The terms for using Predawn and Predawn Pro.", "terms-of-service.html", TERMS),
 "support.html": page("Predawn Support", "Help with Predawn: the forecast, planning, alerts and Predawn Pro.", "support.html", SUPPORT),
}
for name, html in files.items():
    open(os.path.join(OUT, name), "w").write(html)
open(os.path.join(OUT, "README.md"), "w").write("# predawn-site\n\nMarketing, support, privacy and terms pages for Predawn, served by GitHub Pages at " + BASE + ".\n\nGenerated by `build_site.py`; edit that and rebuild.\n")
open(os.path.join(OUT, ".nojekyll"), "w").write("")
print("wrote", ", ".join(files))
