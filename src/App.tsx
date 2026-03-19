import {
  BarChart3,
  Brain,
  CheckCircle2,
  Code2,
  FileText,
  ImageIcon,
  Layers3,
  Lightbulb,
  Link as LinkIcon,
  Network,
  Rocket,
  ShieldCheck,
  Sparkles,
  Target,
  Users,
  Wrench,
} from 'lucide-react';
import { projectData } from './data/projectData';

function SectionHeader({ eyebrow, title, description }: { eyebrow: string; title: string; description: string }) {
  return (
    <div className="section-header">
      <p className="eyebrow">{eyebrow}</p>
      <h2>{title}</h2>
      <p className="section-description">{description}</p>
    </div>
  );
}

function PlaceholderGalleryCard({ title, caption, placeholder }: { title: string; caption: string; placeholder: string }) {
  return (
    <div className="surface gallery-card">
      <div className="gallery-placeholder">
        <div className="gallery-placeholder-inner">
          <ImageIcon size={28} />
          <p>{placeholder}</p>
        </div>
      </div>
      <div className="gallery-body">
        <h3>{title}</h3>
        <p>{caption}</p>
      </div>
    </div>
  );
}

export default function App() {
  return (
    <div className="page-shell">
      <div className="page-container">
        <section className="hero surface hero-surface">
          <div className="hero-copy">
            <div className="template-pill">
              <Sparkles size={14} />
              MSIS 522 — University of Washington
            </div>
            <h1>{projectData.title}</h1>
            <p className="owner-line">{projectData.ownerLine}</p>
            <p className="hero-subtitle">{projectData.subtitle}</p>
            <p className="hero-summary">{projectData.executiveSummary}</p>

            <div className="badge-row">
              {projectData.badges.map((badge) => (
                <span key={badge} className="chip">
                  {badge}
                </span>
              ))}
            </div>

            <div className="link-row">
              {projectData.links.map((link) => (
                <a
                  key={`${link.label}-${link.url}`}
                  href={link.url}
                  className={link.primary ? 'primary-link' : 'secondary-link'}
                  target="_blank"
                  rel="noreferrer"
                >
                  <LinkIcon size={16} />
                  {link.label}
                </a>
              ))}
            </div>
          </div>
        </section>

        <section className="surface instructions-surface">
          <div className="instruction-heading">
            <div className="icon-box cyan-box">
              <FileText size={22} />
            </div>
            <div>
              <p className="instruction-title">How to experience LinkedOut</p>
              <p className="instruction-subtitle">A live AI avatar you can talk to — no scheduling required.</p>
            </div>
          </div>

          <div className="instruction-list">
            {projectData.instructions.map((instruction) => (
              <div key={instruction} className="instruction-card">
                <CheckCircle2 size={20} />
                <p>{instruction}</p>
              </div>
            ))}
          </div>

          <div className="metrics-grid">
            {projectData.metrics.map((metric) => (
              <div key={metric.label} className="metric-card">
                <p className="metric-label">{metric.label}</p>
                <p className="metric-value">{metric.value}</p>
                <p className="metric-note">{metric.note}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="two-col-grid">
          <div className="surface padded-card">
            <div className="card-heading">
              <div className="icon-box emerald-box">
                <Target size={18} />
              </div>
              <div>
                <p className="eyebrow">Problem</p>
                <h3>What problem are you trying to solve?</h3>
              </div>
            </div>
            <p className="body-copy">{projectData.problemStatement}</p>
            <div className="meta-grid">
              <div className="mini-panel">
                <p className="mini-label">Audience</p>
                <p>{projectData.audience}</p>
              </div>
              <div className="mini-panel">
                <p className="mini-label">Impact Goal</p>
                <p>{projectData.impactGoal}</p>
              </div>
              <div className="mini-panel">
                <p className="mini-label">Status</p>
                <p>{projectData.status}</p>
              </div>
            </div>
          </div>

          <div className="dark-card padded-card">
            <div className="card-heading">
              <div className="icon-box dark-icon-box">
                <Lightbulb size={18} />
              </div>
              <div>
                <p className="dark-eyebrow">Solution</p>
                <h3>What are you building?</h3>
              </div>
            </div>
            <p className="dark-copy">{projectData.solutionSummary}</p>
            <div className="method-row">
              {projectData.methods.map((method) => (
                <span key={method} className="dark-chip">
                  {method}
                </span>
              ))}
            </div>
          </div>
        </section>

        <section>
          <SectionHeader
            eyebrow="Team"
            title="Who built LinkedOut"
            description="Four students from the UW MSIS program."
          />
          <div className="card-grid two-up">
            {projectData.members.map((member) => (
              <div key={`${member.name}-${member.role}`} className="surface padded-card team-card">
                <div className="team-avatar">{member.name.replace(/[[\]]/g, '').split(' ').filter(Boolean).map((part) => part[0]).join('').slice(0, 2).toUpperCase() || 'TM'}</div>
                <div>
                  <h3>{member.name}</h3>
                  {member.role && <p className="team-role">{member.role}</p>}
                  <p className="body-copy compact">{member.focus}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        <section>
          <SectionHeader
            eyebrow="Gallery"
            title="See LinkedOut in action"
            description="Screenshots of the live portfolio and avatar interface, plus the system architecture diagram showing exactly how the real-time pipeline is wired together."
          />
          <div className="card-grid two-up">
            {projectData.gallery.map((item) =>
              item.assetPath ? (
                <div key={item.title} className="surface gallery-card">
                  <div className="gallery-image-wrap">
                    <img src={item.assetPath} alt={item.title} className="gallery-image" />
                  </div>
                  <div className="gallery-body">
                    <h3>{item.title}</h3>
                    <p>{item.caption}</p>
                  </div>
                </div>
              ) : (
                <PlaceholderGalleryCard
                  key={item.title}
                  title={item.title}
                  caption={item.caption}
                  placeholder={item.placeholder ?? 'Add a visual asset here'}
                />
              ),
            )}
          </div>
        </section>

        <section className="two-col-grid">
          <div className="surface padded-card">
            <div className="card-heading">
              <div className="icon-box lab-box">
                <Wrench size={18} />
              </div>
              <div>
                <p className="eyebrow">Stack</p>
                <h3>What LinkedOut is built on</h3>
              </div>
            </div>
            <div className="stack-list">
              {projectData.stack.map((group) => (
                <div key={group.category} className="stack-card">
                  <div className="stack-title-row">
                    <Layers3 size={16} />
                    <h4>{group.category}</h4>
                  </div>
                  <div className="badge-row compact-row">
                    {group.tools.map((tool) => (
                      <span key={tool} className="chip">
                        {tool}
                      </span>
                    ))}
                  </div>
                  <p className="body-copy compact">{group.note}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="surface padded-card">
            <div className="card-heading">
              <div className="icon-box violet-box">
                <Brain size={18} />
              </div>
              <div>
                <p className="eyebrow">Methods</p>
                <h3>Key techniques powering the experience</h3>
              </div>
            </div>
            <div className="method-grid">
              {projectData.methods.map((method) => (
                <div key={method} className="method-card">
                  <div className="method-icon">
                    <Sparkles size={14} />
                  </div>
                  <div>
                    <p className="method-title">{method}</p>
                    <p className="method-note">A core part of the LinkedOut real-time avatar pipeline.</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section>
          <SectionHeader
            eyebrow="Product"
            title="What LinkedOut delivers"
            description="Four distinct experiences — live avatar chat, real-time transcription, secure session management, and a full candidate portfolio — all in a single, fast-loading site."
          />
          <div className="card-grid two-up">
            {projectData.features.map((feature) => (
              <div key={feature.title} className="surface padded-card">
                <div className="icon-box cyan-box">
                  <Rocket size={18} />
                </div>
                <h3>{feature.title}</h3>
                <p className="body-copy compact">{feature.description}</p>
                <div className="check-list">
                  {feature.highlights.map((highlight) => (
                    <div key={highlight} className="check-item">
                      <CheckCircle2 size={16} />
                      <p>{highlight}</p>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </section>

        <section className="two-col-grid">
          <div className="surface padded-card">
            <div className="card-heading">
              <div className="icon-box lab-box">
                <Network size={18} />
              </div>
              <div>
                <p className="eyebrow">Architecture</p>
                <h3>How the real-time pipeline works</h3>
              </div>
            </div>
            <div className="architecture-list">
              {projectData.architecture.map((step, index) => (
                <div key={step.title} className="architecture-card">
                  <div className="step-badge">{index + 1}</div>
                  <div>
                    <h4>{step.title}</h4>
                    <p>{step.description}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="surface padded-card">
            <div className="card-heading">
              <div className="icon-box cyan-box">
                <Code2 size={18} />
              </div>
              <div>
                <p className="eyebrow">Code Highlights</p>
                <h3>Key implementation details</h3>
              </div>
            </div>
            <div className="code-list">
              {projectData.codeHighlights.map((snippet) => (
                <div key={snippet.title} className="code-card">
                  <div className="code-card-top">
                    <div>
                      <h4>{snippet.title}</h4>
                      <p>{snippet.note}</p>
                    </div>
                    <span className="language-pill">{snippet.language}</span>
                  </div>
                  <pre>
                    <code>{snippet.code}</code>
                  </pre>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="two-col-grid">
          <div className="surface padded-card">
            <div className="card-heading">
              <div className="icon-box cyan-box">
                <BarChart3 size={18} />
              </div>
              <div>
                <p className="eyebrow">Roadmap</p>
                <h3>Where LinkedOut is headed</h3>
              </div>
            </div>
            <div className="roadmap-list">
              {projectData.roadmap.map((phase) => (
                <div key={phase.phase} className="roadmap-card">
                  <p className="roadmap-phase">{phase.phase}</p>
                  <div className="roadmap-items">
                    {phase.items.map((item) => (
                      <div key={item} className="bullet-item">
                        <span />
                        <p>{item}</p>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="surface padded-card">
            <div className="card-heading">
              <div className="icon-box danger-box">
                <ShieldCheck size={18} />
              </div>
              <div>
                <p className="eyebrow">Risks</p>
                <h3>Risks and how they are managed</h3>
              </div>
            </div>
            <div className="risk-list">
              {projectData.risks.map((risk) => (
                <div key={risk.title} className="risk-card">
                  <h4>{risk.title}</h4>
                  <p>{risk.mitigation}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="closing-card">
          <div>
            <p className="dark-eyebrow">The Bottom Line</p>
            <h2>LinkedOut: a portfolio that talks back</h2>
            <p>
              The job search is broken for strong communicators who get filtered out before a human ever hears them.
              LinkedOut fixes that — a live AI avatar, always available, representing the candidate with depth and personality.
            </p>
          </div>

          <div className="card-grid two-up">
            <div className="closing-mini-card">
              <div className="icon-box dark-icon-box">
                <Users size={18} />
              </div>
              <h3>Who benefits?</h3>
              <p>Recruiters and hiring managers get richer signal faster. Candidates get a 24/7 voice — no meeting needed.</p>
            </div>
            <div className="closing-mini-card">
              <div className="icon-box dark-icon-box">
                <Target size={18} />
              </div>
              <h3>What changes?</h3>
              <p>Screening conversations happen on the recruiter's schedule, not the candidate's calendar — eliminating scheduling friction entirely.</p>
            </div>
            <div className="closing-mini-card">
              <div className="icon-box dark-icon-box">
                <Layers3 size={18} />
              </div>
              <h3>Why this build?</h3>
              <p>LiveKit WebRTC + ElevenLabs means the avatar interaction is real-time and lifelike — not a chatbot, not a recording, but a live conversation.</p>
            </div>
            <div className="closing-mini-card">
              <div className="icon-box dark-icon-box">
                <Rocket size={18} />
              </div>
              <h3>What is next?</h3>
              <p>RAG grounding over the candidate's verified documents, recruiter-facing session replays, and a multi-candidate platform for agencies.</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}
