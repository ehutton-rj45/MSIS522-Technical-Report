export interface ProjectLink {
  label: string;
  url: string;
  primary?: boolean;
}

export interface ProjectMetric {
  label: string;
  value: string;
  note: string;
}

export interface TeamMember {
  name: string;
  role: string;
  focus: string;
}

export interface GalleryItem {
  title: string;
  caption: string;
  assetPath?: string;
  placeholder?: string;
}

export interface StackGroup {
  category: string;
  tools: string[];
  note: string;
}

export interface FeatureCard {
  title: string;
  description: string;
  highlights: string[];
}

export interface ArchitectureItem {
  title: string;
  description: string;
}

export interface CodeHighlight {
  title: string;
  language: string;
  note: string;
  code: string;
}

export interface RoadmapPhase {
  phase: string;
  items: string[];
}

export interface RiskItem {
  title: string;
  mitigation: string;
}

export interface ProjectPageData {
  slug: string;
  title: string;
  subtitle: string;
  ownerLine: string;
  executiveSummary: string;
  instructions: string[];
  links: ProjectLink[];
  badges: string[];
  methods: string[];
  metrics: ProjectMetric[];
  problemStatement: string;
  solutionSummary: string;
  audience: string;
  impactGoal: string;
  status: string;
  keywords: string[];
  members: TeamMember[];
  gallery: GalleryItem[];
  stack: StackGroup[];
  features: FeatureCard[];
  architecture: ArchitectureItem[];
  codeHighlights: CodeHighlight[];
  roadmap: RoadmapPhase[];
  risks: RiskItem[];
}

// Students: this is the main file you should edit.
// Replace every bracketed placeholder with real content.
// Put screenshots, PDFs, and diagrams in public/project-assets/.
// In most cases, you do not need to edit App.tsx or styles.css.

export const projectData: ProjectPageData = {
  slug: 'linkedout',

  // Basic page identity
  title: 'LinkedOut',
  subtitle:
    'An AI-powered interactive portfolio that lets recruiters and hiring teams talk live to a digital avatar of the candidate — anytime, without scheduling.',
  ownerLine: 'Hardik Sharma, Aria Wang, Ethan Hutton & Jingying Deng — MSIS 522, University of Washington',
  executiveSummary:
    'LinkedOut reimagines the job-search portfolio as a two-way conversation. Instead of a static resume page, hiring managers and recruiters visit a personal website and instantly connect with a real-time AI video avatar of the candidate. The avatar is powered by the LiveAvatar API and orchestrated by an ElevenLabs Conversational Agent, and it streams audio and video through a LiveKit room so the interaction feels like a live video call. A lightweight Node/Express backend handles session lifecycle securely, while a clean HTML/CSS/JS frontend keeps the experience fast and frictionless. The core insight is that recruiters make decisions on personality and communication as much as credentials — LinkedOut closes that gap by letting candidates "be present" 24/7 without engineering a live meeting.',

  // Short instruction cards removed — replaced with real project context
  instructions: [
    'Start a session on the "Talk to Me" page and speak directly with the AI avatar.',
    'Explore the Projects and Skills pages to see a full breakdown of background and capabilities.',
    'Use Push-to-Talk or Open-Mic mode — the avatar responds in real time via ElevenLabs voice.',
    'The session runs for a timed window; click End Session or let it expire gracefully.',
  ],

  // Main action buttons / links
  links: [
    { label: 'Live Demo', url: 'https://github.com/hdksrma/theportfolioproject', primary: true },
    { label: 'GitHub Repo', url: 'https://github.com/hdksrma/theportfolioproject' },
    { label: 'Technical Report', url: '/project-assets/Technical report.pdf' },
    { label: 'Slide Deck', url: '/project-assets/MSIS 522 Project_LinkedOut.pptx' },
  ],

  badges: [
    'Node.js / Express',
    'LiveAvatar API',
    'LiveKit WebRTC',
    'ElevenLabs Agent',
    'HTML / CSS / JS',
    'Conversational AI',
  ],

  keywords: ['ai-avatar', 'portfolio', 'conversational-ai', 'webrtc', 'liveavatar', 'elevenlabs'],

  methods: [
    'Real-time WebRTC streaming',
    'Conversational AI agent',
    'Push-to-Talk & Open-Mic interaction',
    'Session token management',
    'Live transcript & event logging',
  ],

  metrics: [
    { label: 'Core User', value: 'Recruiters & Hiring Managers', note: 'Anyone who reviews candidates asynchronously' },
    { label: 'Availability', value: '24 / 7', note: 'Avatar is always on — no scheduling required' },
    { label: 'Response Latency', value: 'Real-time', note: 'Streamed via LiveKit WebRTC, sub-second turns' },
    { label: 'Status', value: 'Live Prototype', note: 'Deployed and functional end-to-end' },
  ],

  problemStatement:
    'Job seekers spend enormous effort crafting static resumes and portfolio sites — yet recruiters still cannot get a sense of how someone communicates, thinks, or presents themselves without scheduling a screening call. Scheduling friction, time-zone gaps, and high candidate volume mean many strong candidates are screened out before a human ever speaks to them. Traditional async video recordings feel stiff and one-directional. There is no way for a recruiter to ask a follow-up question, probe for depth, or test how a candidate handles a novel prompt — all the signals that matter most in early screening.',
  solutionSummary:
    'LinkedOut replaces the static portfolio with a live, conversational AI avatar that represents the candidate on demand. A recruiter visits the site, clicks "Start Session," and is immediately connected to a streaming video avatar trained on the candidate\'s background, projects, and communication style. The avatar handles push-to-talk or open-mic input, responds via ElevenLabs voice synthesis, and transcribes the conversation in real time. The candidate\'s actual identity — their experience, projects, and technical depth — is encoded into the avatar\'s context so that every answer is authentic and personalized.',
  audience: 'Recruiters, hiring managers, and technical interviewers reviewing software engineering candidates',
  impactGoal:
    'Reduce time-to-first-meaningful-conversation for candidates, lower scheduling overhead for recruiters, and help strong communicators stand out from a sea of identical résumés.',
  status: 'Live Prototype',

  members: [
    {
      name: 'Hardik Sharma',
      role: '',
      focus:
        'Built the full Node.js/Express backend, integrated the LiveAvatar API, wired up the LiveKit WebRTC room to carry video, audio, and bidirectional data events, tuned the ElevenLabs agent persona, crafted the context prompts and conversational flow.',
    },
    {
      name: 'Aria Wang',
      role: '',
      focus:
        'Built the demo day presentation. Synthesized the full project into a compelling narrative for stakeholders, designed the slide deck structure and visual story, and prepared the live demonstration flow for the class presentation.',
    },
    {
      name: 'Ethan Hutton',
      role: '',
      focus:
        "Built the Technical Report based off the professor's template. Documented the project in a structured academic format aligned with MSIS 522 course requirements.",
    },
    {
      name: 'Jingying Deng',
      role: '',
      focus:
        "Led the live demonstration during the demo day presentation, showcased the avatar's real-time conversational capabilities to the class, and fielded questions from the audience.",
    },
  ],

  gallery: [
    {
      title: 'Portfolio Home — Hardik Sharma',
      caption:
        'The landing page presents the candidate\'s headline, key impact stats, experience, and education in a clean dark-mode layout. A prominent "Talk to my avatar" CTA drives visitors directly to the live avatar experience.',
      assetPath: '/project-assets/Screenshot 2026-03-18 213242.jpg',
    },
    {
      title: 'Live Avatar — Session Starting',
      caption:
        'The "Talk to Me" page loads the avatar stream interface. Controls for Start Session, Hold to Talk, and End Session are clearly visible alongside a live status strip showing connection, mic, session ID, and countdown timer.',
      assetPath: '/project-assets/Screenshot 2026-03-18 213316.jpg',
    },
    {
      title: 'Live Avatar — Active Conversation',
      caption:
        'Once the session is connected, the avatar\'s face appears in the video panel and begins speaking. The Live Transcript panel captures every turn, and the Event Stream shows the raw LiveKit data events in real time.',
      assetPath: '/project-assets/Screenshot 2026-03-18 213331.jpg',
    },
    {
      title: 'System Architecture Diagram',
      caption:
        'Data flow from browser mic/UI → Portfolio Frontend → Node/Express Backend → LiveAvatar API → LiveKit Room, with ElevenLabs Agent handling conversational processing and Plugin Worker orchestrating the avatar\'s responses.',
      assetPath: '/project-assets/MSIS-522-Project-Code/theportfolioproject-main/mermaid-diagram.png',
    },
  ],

  stack: [
    {
      category: 'Frontend and Experience',
      tools: ['HTML5', 'CSS3 (custom dark-mode design system)', 'Vanilla JavaScript', 'Space Grotesk / Space Mono fonts'],
      note:
        'Zero-framework frontend keeps the bundle tiny and load instant. Custom CSS variables handle the dark-mode palette, glassmorphism cards, and responsive layout without a CSS framework.',
    },
    {
      category: 'AI, Avatar, and Real-Time Communication',
      tools: ['LiveAvatar API (session token + start/stop)', 'ElevenLabs Conversational Agent', 'LiveKit WebRTC (video + audio + data channel)', 'livekit-client JS SDK'],
      note:
        'LiveAvatar API provisions a streaming session token. LiveKit sets up the WebRTC room that carries video (avatar face), audio (ElevenLabs voice), and bidirectional data events. ElevenLabs handles speech synthesis and conversational context.',
    },
    {
      category: 'Backend and Infrastructure',
      tools: ['Node.js', 'Express', 'dotenv (secrets management)', 'Static file serving'],
      note:
        'The Express server acts as a secure proxy between the browser and the LiveAvatar API so that the API key never reaches the client. Two endpoints handle the full session lifecycle: POST /api/session (create + start) and POST /api/session/stop.',
    },
  ],

  features: [
    {
      title: 'Live Video Avatar Chat',
      description:
        'Visitors click "Start Session" and within seconds are face-to-face with a lifelike video avatar of the candidate. The avatar speaks, listens, and responds to natural questions about the candidate\'s background, skills, and projects.',
      highlights: [
        'Push-to-Talk (spacebar or button) and Open-Mic modes for flexible interaction',
        'ElevenLabs voice synthesis delivers natural, low-latency speech output',
        'LiveKit WebRTC streams video and audio with sub-second latency',
      ],
    },
    {
      title: 'Live Transcript & Event Stream',
      description:
        'Every conversation turn is captured and displayed in real time. A Live Transcript panel shows user and avatar utterances side-by-side. A separate Event Stream panel renders raw JSON events from the LiveKit data channel so power users can inspect the session.',
      highlights: [
        'User and avatar transcript lines distinguished by role labels',
        'Events logged include speak_started, speak_ended, transcription, and mic state',
        'Full session event history remains visible for the duration of the call',
      ],
    },
    {
      title: 'Secure Session Management',
      description:
        'The Node/Express backend handles all credential operations server-side. The browser never touches an API key. Session tokens are minted per call, and both /api/session and /api/session/stop follow a clean create-start-stop lifecycle.',
      highlights: [
        'API key stored in .env, never exposed to the client',
        'Session stop is called on End Session click AND on browser unload via sendBeacon',
        'UUID validation guards avatar_id and voice_id inputs before forwarding to LiveAvatar',
      ],
    },
    {
      title: 'Candidate Portfolio Pages',
      description:
        'Alongside the avatar, the site ships full portfolio pages: a Home page with impact stats, an Experience timeline, a Projects gallery with modal detail overlays, and a Skills breakdown across languages, cloud, AI/ML, and agent systems.',
      highlights: [
        'Impact stats: 20+ hrs/week saved, 90% faster retrieval, 95% overhead reduction',
        'Projects page covers RAG platform, LLM fine-tuning, autonomous trading system, and more',
        'Skills page spans Python/JS/C++, AWS, LangGraph, CrewAI, Pinecone, and MLflow',
      ],
    },
  ],

  architecture: [
    {
      title: 'User Input (Browser)',
      description:
        'The visitor uses mic controls (Push-to-Talk or Open-Mic) on talk.html. The livekit-client SDK publishes local audio tracks to the LiveKit room and sends control events (user.start_push_to_talk, avatar.start_listening) over a data channel.',
    },
    {
      title: 'Session Provisioning (Node/Express)',
      description:
        'POST /api/session calls the LiveAvatar API in two steps: first minting a session token (with avatar_id, voice_id, context_id, and interactivity_type), then starting the session. The backend returns the LiveKit URL and client token to the browser.',
    },
    {
      title: 'Real-Time Streaming (LiveKit Room)',
      description:
        'The browser connects to the LiveKit room using the returned URL and token. The avatar\'s video and audio tracks are subscribed and rendered into the DOM. Data events flow bidirectionally for transcription, speak_started/ended, and push-to-talk control.',
    },
    {
      title: 'Conversational AI (LiveAvatar + ElevenLabs Agent)',
      description:
        'LiveAvatar\'s Plugin Worker routes the session to an ElevenLabs Agent that handles speech recognition, context retrieval, and response generation. The agent\'s output is synthesized into voice, lipsynced to the avatar video, and streamed back through LiveKit.',
    },
  ],

  codeHighlights: [
    {
      title: 'Backend: Two-Step Session Creation',
      language: 'js',
      note:
        'The Express proxy mints a session token then immediately starts the session, returning both the LiveKit URL/token and session metadata to the browser in a single response.',
      code: `// Step 1 — mint a session token
const tokenResp = await fetch(\`\${LIVEAVATAR_BASE_URL}/v1/sessions/token\`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', 'X-API-KEY': LIVEAVATAR_API_KEY },
  body: JSON.stringify({
    mode: 'FULL',
    avatar_id: AVATAR_ID,
    interactivity_type: 'PUSH_TO_TALK',
    avatar_persona: { voice_id, context_id, language }
  })
});
const { session_token, session_id } = await tokenResp.json();

// Step 2 — activate the session
const startResp = await fetch(\`\${LIVEAVATAR_BASE_URL}/v1/sessions/start\`, {
  method: 'POST',
  headers: { Authorization: \`Bearer \${session_token}\` },
  body: JSON.stringify({})
});
return res.json({ session_id, session_token, ...await startResp.json() });`,
    },
    {
      title: 'Frontend: LiveKit Track Subscription & Avatar Render',
      language: 'js',
      note:
        'When the LiveKit room publishes tracks, video is attached to the avatar div and audio to the document body so playback is automatic and the UI stays clean.',
      code: `room.on(RoomEvent.TrackSubscribed, (track) => {
  if (track.kind === 'video') {
    const el = track.attach();
    el.style.width = '100%';
    el.style.height = '100%';
    avatarEl.innerHTML = '';
    avatarEl.appendChild(el);       // avatar face renders here
  } else if (track.kind === 'audio') {
    const el = track.attach();
    el.style.display = 'none';
    document.body.appendChild(el);  // hidden audio element auto-plays
  }
});`,
    },
  ],

  roadmap: [
    {
      phase: 'Now',
      items: [
        'Fully functional live avatar with Push-to-Talk and Open-Mic modes',
        'Secure Express backend handling session lifecycle for the LiveAvatar API',
        'Static portfolio pages: Home, Projects (with modal), Skills, and Talk to Me',
        'Live transcript and raw event stream visible during every session',
      ],
    },
    {
      phase: 'Next',
      items: [
        'Add a context document upload so any candidate can configure their own avatar persona without code',
        'Integrate a RAG layer over the candidate\'s resume, portfolio, and GitHub repos for deeper, citation-backed answers',
        'Recruiter-facing session replay and summary so hiring teams can share and annotate avatar conversations',
        'Analytics dashboard tracking which questions were asked most and where sessions ended',
      ],
    },
    {
      phase: 'Later',
      items: [
        'Multi-candidate platform: a single recruiter interface to "interview" shortlisted candidates back-to-back via their avatars',
        'ATS (Applicant Tracking System) integration to trigger avatar sessions from a job application submit',
        'Mobile-optimized PWA so recruiters can talk to candidates on the go',
        'Bring-your-own-voice fine-tuning so the avatar matches the candidate\'s actual vocal pattern',
      ],
    },
  ],

  risks: [
    {
      title: 'Third-Party API Dependency (LiveAvatar + ElevenLabs)',
      mitigation:
        'The entire avatar experience depends on LiveAvatar API uptime and quota limits. Mitigated by session-level error handling, graceful "session failed" UI states, and a fallback text-chat mode so the portfolio remains usable if the stream is unavailable.',
    },
    {
      title: 'Context Drift & Hallucination',
      mitigation:
        'Conversational agents can generate plausible but incorrect answers about the candidate. Mitigated by a tightly scoped persona context injected at session creation, and future work to add a RAG grounding layer over verified documents.',
    },
    {
      title: 'Session Cost and Latency at Scale',
      mitigation:
        'LiveAvatar streaming sessions carry per-minute API costs. At low traffic (portfolio use case) this is negligible, but viral exposure could be expensive. Mitigated by session duration caps (countdown timer enforced server-side) and lazy session start.',
    },
    {
      title: 'Browser Microphone Permission & WebRTC Compatibility',
      mitigation:
        'Push-to-talk requires mic access; some corporate networks block WebRTC. Mitigated by a text-input fallback (the Send button) that sends avatar.speak_response events without requiring audio, keeping the core interaction available across environments.',
    },
  ],
};
