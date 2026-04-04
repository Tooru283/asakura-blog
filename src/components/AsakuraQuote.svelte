<script>
  import { onMount } from 'svelte';

  const lines = [
    "海边，去吗？",
    "找到我，好好地",
    "透明的，看不见的东西。不注意的话，就会消失呢",
    "感觉……可以游过去。就在那里吧",
    "稍微，离远一点也可以哦。因为……我知道你在那里",
    "不用着急。这里的时间，是静止的哦",
    "风……好舒服……",
    "你，也是透明的吗？"
  ];

  let currentLine = '';
  let show = false;

  const refreshLine = () => {
    show = false;
    setTimeout(() => {
      const randomIndex = Math.floor(Math.random() * lines.length);
      currentLine = lines[randomIndex];
      show = true;
    }, 300);
  };

  onMount(() => {
    refreshLine();
  });
</script>

<div 
  class="quote-widget" 
  on:click={refreshLine}
  role="button"
  tabindex="0"
  on:keydown={(e) => e.key === 'Enter' && refreshLine()}
>
  <span class="quote-dot">·</span>
  <p class="quote-text" class:visible={show}>
    {currentLine || "..."}
  </p>
</div>

<style>
  .quote-widget {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    padding: 0.75rem 1.25rem;
    border-radius: 9999px;
    cursor: pointer;
    z-index: 2000;
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    max-width: 280px;
    min-width: 120px;
    display: flex;
    align-items: center;
    gap: 0.5rem;

    /* Glassmorphism */
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.22);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12), 0 2px 8px rgba(0, 0, 0, 0.08);
  }

  :global([data-theme="dark"]) .quote-widget {
    background: rgba(30, 30, 40, 0.45);
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35), 0 2px 8px rgba(0, 0, 0, 0.2);
  }

  .quote-widget:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.18), 0 4px 12px rgba(0, 0, 0, 0.1);
    background: rgba(255, 255, 255, 0.18);
  }

  :global([data-theme="dark"]) .quote-widget:hover {
    background: rgba(40, 40, 55, 0.6);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45), 0 4px 12px rgba(0, 0, 0, 0.25);
  }

  .quote-dot {
    font-size: 1.2rem;
    opacity: 0.5;
    flex-shrink: 0;
    color: var(--link-color, #7eb8d4);
    line-height: 1;
  }

  .quote-text {
    font-size: 0.8rem;
    opacity: 0;
    transform: translateX(6px);
    transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    text-align: left;
    color: var(--text-color);
    margin: 0;
    line-height: 1.5;
    font-weight: 300;
    letter-spacing: 0.02em;
  }

  .quote-text.visible {
    opacity: 0.85;
    transform: translateX(0);
  }
</style>
