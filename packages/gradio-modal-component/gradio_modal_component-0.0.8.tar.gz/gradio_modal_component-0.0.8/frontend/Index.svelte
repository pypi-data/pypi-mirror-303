<script context="module" lang="ts">
  export { default as BaseButton } from "./shared/Button.svelte";
</script>

<script lang="ts">
  import { Block } from "@gradio/atoms";
  import Column from "@gradio/column";
  import { Gradio } from "@gradio/utils";
  import { onMount } from "svelte";

  import Button from "./shared/Button.svelte";

  interface CloseMessageStyle {
    message_color?: string;
    confirm_text?: string;
    cancel_text?: string;
    confirm_bg_color?: string;
    cancel_bg_color?: string;
    confirm_text_color?: string;
    cancel_text_color?: string;
    modal_bg_color?: string;
    confirm_border_color?: string;
    cancel_border_color?: string;
    height?: string;
    width?: string;
    size?: string;
  }

  export let elem_id = "";
  export let elem_classes: string[] = [];
  export let visible = false;
  export let display_close_icon: boolean = false;
  export let close_on_esc: boolean;
  export let close_outer_click: boolean;
  export let close_message: string;
  export let bg_blur: number;
  export let width: number;
  export let height: number;
  export let content_width_percent: number;
  export let content_height_percent: number;
  export let content_padding: string;
  export let opacity_level: number;
  export let animate: string;
  export let animation_duration: number = 0.4;

  export let gradio: Gradio<{
    blur: never;
  }>;

  export let close_message_style: CloseMessageStyle = {
    message_color: "var(--body-text-color)",
    confirm_text: "Yes",
    cancel_text: "No",
    confirm_bg_color: "var(--primary-500)",
    cancel_bg_color: "var(--neutral-500)",
    confirm_text_color: "white",
    cancel_text_color: "white",
    modal_bg_color: "var(--background-fill-primary)",
  };

  let element: HTMLElement | null = null;
  let inner_element: HTMLElement | null = null;
  let showConfirmation = false;
  let clickX = 0;
  let clickY = 0;
  let containerRect: DOMRect | null = null;

  onMount(() => {
    // Track click position for animations
    document.addEventListener("click", (e) => {
      if (!visible) {
        clickX = e.clientX;
        clickY = e.clientY;
      }
    });
  });

  function getAnimationClass() {
    if (!animate) return "";

    switch (animate.toLowerCase()) {
      case "zoom in":
        return "modal-zoom";
      case "top":
        return "modal-top";
      case "bottom":
        return "modal-bottom";
      case "left":
        return "modal-left";
      case "right":
        return "modal-right";
      case "fade in":
        return "modal-fade";
      default:
        return "";
    }
  }

  function getAnimationOrigin() {
    if (!containerRect) return "";

    const centerX = Math.max(0, Math.min(clickX, window.innerWidth));
    const centerY = Math.max(0, Math.min(clickY, window.innerHeight));

    return `transform-origin: ${centerX}px ${centerY}px;`;
  }

  const close = () => {
    if (close_message) {
      showConfirmation = true;
    } else {
      closeModal();
    }
  };

  const closeModal = () => {
    visible = false;
    showConfirmation = false;
    gradio.dispatch("blur");
  };

  const cancelClose = () => {
    showConfirmation = false;
  };

  document.addEventListener("keydown", (evt: KeyboardEvent) => {
    if (close_on_esc && evt.key === "Escape") {
      close();
    }
  });

  $: if (inner_element) {
    containerRect = inner_element.getBoundingClientRect();
  }

  $: modalStyle = `
    backdrop-filter: blur(${bg_blur}px);
    -webkit-backdrop-filter: blur(${bg_blur}px);
    background-color: rgba(0, 0, 0, ${opacity_level});
    --animation-duration: ${animation_duration}s;
  `;

  $: containerStyle = `
    width: ${width}px;
    height: ${height}px;
    animation-duration: ${animation_duration}s;
    ${getAnimationOrigin()}
  `;

  $: contentStyle = (() => {
    const paddingStyle = content_padding ? `${content_padding}` : "0px";
    const widthStyle = content_width_percent
      ? `${content_width_percent}%`
      : "100%";
    const heightStyle = content_height_percent
      ? `${content_height_percent}%`
      : "100%";
    return `width: ${widthStyle}; max-height: ${heightStyle}; padding: ${paddingStyle};`;
  })();

  $: {
    console.log("bg_blue", bg_blur);
    console.log("opacity_level", opacity_level);
  }

  document.addEventListener("keydown", (evt: KeyboardEvent) => {
    if (close_on_esc && evt.key === "Escape") {
      close();
    }
  });
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
  class="modal {elem_classes.join(' ')} {getAnimationClass()}"
  bind:this={element}
  class:hide={!visible}
  id={elem_id}
  style={modalStyle}
  on:click={(evt) => {
    if (
      close_outer_click &&
      (evt.target === element || evt.target === inner_element)
    ) {
      close();
    }
  }}
>
  <div class="modal-container" bind:this={inner_element} style={containerStyle}>
    <Block allow_overflow={false} elem_classes={["modal-block"]}>
      {#if display_close_icon}
        <div class="close" on:click={close}>
          <svg
            width="10"
            height="10"
            viewBox="0 0 10 10"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M1 1L9 9"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
            <path
              d="M9 1L1 9"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </div>
      {/if}
      <div class="modal-content" style={contentStyle}>
        <Column elem_classes={["centered-column"]}>
          <slot />
        </Column>
      </div>
    </Block>
  </div>
  {#if showConfirmation}
    <div class="confirmation-modal">
      <div
        class="confirmation-content"
        style="background-color: {close_message_style.modal_bg_color}"
      >
        <h3 style="color: {close_message_style.message_color}">
          {close_message}
        </h3>
        <br />
        <div class="confirmation-buttons">
          <Button
            class_name="no-button"
            on:click={cancelClose}
            background_color={close_message_style.cancel_bg_color}
            color={close_message_style.cancel_text_color}
            border_color={close_message_style.cancel_border_color}
            width={close_message_style.width}
            height={close_message_style.height}
            size={close_message_style.size}
          >
            {close_message_style.cancel_text}
          </Button>
          <Button
            class_name="yes-button"
            on:click={closeModal}
            background_color={close_message_style.confirm_bg_color}
            color={close_message_style.confirm_text_color}
            border_color={close_message_style.confirm_border_color}
            width={close_message_style.width}
            height={close_message_style.height}
            size={close_message_style.size}
          >
            {close_message_style.confirm_text}
          </Button>
        </div>
      </div>
    </div>
  {/if}
</div>

<style>
  @media (min-width: 640px) {
    .modal-container {
      max-width: 640px;
    }
  }

  @media (min-width: 768px) {
    .modal-container {
      max-width: 768px;
    }
  }

  @media (min-width: 1024px) {
    .modal-container {
      max-width: 1024px;
    }
  }

  @media (min-width: 1280px) {
    .modal-container {
      max-width: 1280px;
    }
  }

  @media (min-width: 1536px) {
    .modal-container {
      max-width: 1536px;
    }
  }

  .modal {
    position: fixed;
    z-index: 500;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(4px);
  }

  .modal {
    position: fixed;
    z-index: 500;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
  }

  /* Animation classes */
  .modal-zoom .modal-container {
    animation: zoom-in var(--animation-duration, 0.4s) ease-out;
  }

  .modal-top .modal-container {
    animation: slide-top var(--animation-duration, 0.4s) ease-out;
  }

  .modal-bottom .modal-container {
    animation: slide-bottom var(--animation-duration, 0.4s) ease-out;
  }

  .modal-left .modal-container {
    animation: slide-left var(--animation-duration, 0.4s) ease-out;
  }

  .modal-right .modal-container {
    animation: slide-right var(--animation-duration, 0.4s) ease-out;
  }

  .modal-fade {
    animation: fade-in var(--animation-duration, 0.4s) ease-out;
  }

  /* Animation keyframes */
  @keyframes zoom-in {
    from {
      transform: scale(0);
      opacity: 0;
    }
    to {
      transform: scale(1);
      opacity: 1;
    }
  }

  @keyframes slide-top {
    from {
      transform: translateY(-50px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }

  @keyframes slide-bottom {
    from {
      transform: translateY(50px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }

  @keyframes slide-left {
    from {
      transform: translateX(-50px);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }

  @keyframes slide-right {
    from {
      transform: translateX(50px);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }

  @keyframes fade-in {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  .modal-container {
    position: relative;
    padding: 0 var(--size-8);
    margin: var(--size-8) auto;
    width: 100%;
    height: 100%;
    max-height: calc(100% - var(--size-16));
    max-width: calc(100% - var(--size-16));
    overflow-y: hidden;
    display: flex;
    width: 100%;
    height: 100%;
    justify-items: center;
    align-items: start;
  }
  .close {
    position: absolute;
    top: var(--block-label-margin);
    right: var(--block-label-margin);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: var(--shadow-drop);
    border: 1px solid var(--border-color-primary);
    border-top: none;
    border-right: none;
    border-radius: var(--block-label-right-radius);
    background: var(--block-label-background-fill);
    padding: 6px;
    width: 24px;
    height: 24px;
    color: var(--block-label-text-color);
    font: var(--font);
    font-size: var(--button-small-text-size);
    cursor: pointer;
    z-index: 2;
  }
  .modal-content {
    padding-top: calc(24px + var(--block-label-margin) * 2);
    margin: 10px;
    width: 100%;
    height: 100%;
    display: flex;
    justify-items: center;
  }

  .modal :global(.modal-block) {
    display: flex;
    justify-content: center;
    max-height: 100%;
    overflow-y: auto !important;
  }

  .modal :global(.centered-column) {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
  }
  .hide {
    display: none;
  }

  .confirmation-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 600;
  }

  .confirmation-content {
    background-color: var(--background-fill-primary);
    color: var(--body-text-color);
    padding: 2rem;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-drop-lg);
    text-align: center;
    width: 90%;
    max-width: 400px;
  }

  .confirmation-content h3 {
    margin-top: 0;
    font-size: var(--text-lg);
    font-weight: var(--weight-medium);
  }

  .confirmation-buttons{
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 1rem;
  }
  .confirmation-buttons button {
    padding: 0.5rem 1.5rem;
    border: none;
    border-radius: var(--radius-md);
    cursor: pointer;
    font-size: var(--text-sm);
    font-weight: var(--weight-medium);
    transition: background-color 0.3s ease;
  }

  .confirmation-buttons .yes-button {
    background-color: var(--primary-500);
    color: white;
    box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.1);
  }

  .confirmation-buttons .yes-button:hover {
    background-color: var(--primary-600);
  }

  .confirmation-buttons .no-button {
    background-color: gray;
    color: white;
    box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.1);
  }

  .confirmation-buttons .no-button:hover {
    background-color: darkgray;
  }
</style>
