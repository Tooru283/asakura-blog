<script>
  import { onMount } from "svelte";

  let isPlaying = false;
  let audioRef;
  // A calm, deep ocean wave ambiance loop
  // 使用网易云音乐的直链解析 API
  const src = "https://music.163.com/song/media/outer/url?id=1831032925.mp3";

  const togglePlay = () => {
    if (isPlaying) {
      audioRef.pause();
    } else {
      audioRef.play().catch((e) => console.error("Audio play blocked", e));
    }
    isPlaying = !isPlaying;
  };
</script>

<div
  class="ambient-player"
  class:playing={isPlaying}
  on:click={togglePlay}
  role="button"
  tabindex="0"
  on:keydown={(e) => e.key === "Enter" && togglePlay()}
>
  <audio bind:this={audioRef} {src} loop preload="none"></audio>

  <div class="icon-wrapper">
    {#if isPlaying}
      <div class="bars">
        <span class="bar bar1"></span>
        <span class="bar bar2"></span>
        <span class="bar bar3"></span>
      </div>
    {:else}
      <svg viewBox="0 0 24 24" class="play-icon">
        <path fill="currentColor" d="M8 5v14l11-7z" />
      </svg>
    {/if}
  </div>

  <div class="info">
    <span class="track-name">/// Statice</span>
  </div>
</div>

<style>
  .ambient-player {
    position: fixed;
    bottom: 6.5rem; /* Placed exactly above AsakuraQuote widget */
    right: 2rem;
    padding: 0.6rem 1.2rem;
    border-radius: 9999px;
    cursor: pointer;
    z-index: 2000;
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    display: flex;
    align-items: center;
    gap: 0.75rem;

    /* Glassmorphism base identical to Quote widget for aesthetic matching */
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.22);
    box-shadow:
      0 8px 32px rgba(0, 0, 0, 0.12),
      0 2px 8px rgba(0, 0, 0, 0.08);
  }

  :global([data-theme="dark"]) .ambient-player {
    background: rgba(30, 30, 40, 0.45);
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow:
      0 8px 32px rgba(0, 0, 0, 0.35),
      0 2px 8px rgba(0, 0, 0, 0.2);
  }

  .ambient-player:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow:
      0 16px 40px rgba(0, 0, 0, 0.18),
      0 4px 12px rgba(0, 0, 0, 0.1);
    background: rgba(255, 255, 255, 0.18);
  }

  :global([data-theme="dark"]) .ambient-player:hover {
    background: rgba(40, 40, 55, 0.6);
    box-shadow:
      0 16px 40px rgba(0, 0, 0, 0.45),
      0 4px 12px rgba(0, 0, 0, 0.25);
  }

  /* Breathing light effect when playing */
  .ambient-player.playing {
    border-color: rgba(126, 184, 212, 0.5);
    box-shadow:
      0 8px 32px rgba(126, 184, 212, 0.15),
      0 0 20px rgba(126, 184, 212, 0.2);
  }

  .icon-wrapper {
    width: 20px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--link-color, #7eb8d4);
  }

  .play-icon {
    width: 14px;
    height: 14px;
    opacity: 0.8;
  }

  /* Water ripple dancing bars */
  .bars {
    display: flex;
    align-items: flex-end;
    gap: 3px;
    height: 12px;
  }

  .bar {
    width: 3px;
    background-color: var(--link-color, #7eb8d4);
    border-radius: 2px;
    animation: waveSync 1.2s infinite ease-in-out;
  }

  .bar1 {
    height: 100%;
    animation-delay: 0s;
  }
  .bar2 {
    height: 60%;
    animation-delay: -0.4s;
  }
  .bar3 {
    height: 80%;
    animation-delay: -0.8s;
  }

  @keyframes waveSync {
    0%,
    100% {
      transform: scaleY(0.4);
    }
    50% {
      transform: scaleY(1);
    }
  }

  .track-name {
    font-size: 0.75rem;
    color: var(--text-color);
    letter-spacing: 0.05em;
    font-weight: 300;
    opacity: 0.6;
    transition: opacity 0.3s ease;
  }

  .ambient-player:hover .track-name,
  .ambient-player.playing .track-name {
    opacity: 0.95;
  }
</style>
