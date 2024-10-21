// Utility functions
const Utils = {
  sendInteraction: (type, details) => {
    console.log('Registered event:', type, details);
    window.registerInteraction(type, JSON.stringify(details));
  },

  getBoundingBox: (element) => {
    const { left, top, width, height } = element.getBoundingClientRect();
    return { x: left, y: top, width, height };
  },

  getScrollPosition: () => ({
    scrollLeft: window.pageXOffset || document.documentElement.scrollLeft,
    scrollTop: window.pageYOffset || document.documentElement.scrollTop,
  }),

  getPathTo: (element) => {
    if (!element || element === document.body) {
      return element ? element.tagName.toLowerCase() : '';
    }

    const path = [];
    while (element && element !== document.body) {
      const tagName = element.tagName.toLowerCase();
      let index = 1;

        // Traverse only previous siblings to count elements of the same tag
      for (let sibling = element.previousElementSibling; sibling; sibling = sibling.previousElementSibling) {
            if (sibling.tagName.toLowerCase() === tagName) {
                index++;
            }
      }

      path.push(`${tagName}[${index}]`);
      element = element.parentElement;
    }

    return '/' + path.reverse().join('/');
  },
};

// Event handlers
const EventHandlers = {
  mouseEvent: (e) => ({
    button: e.button,
    x: e.clientX,
    y: e.clientY,
  }),

  keyEvent: (e) => ({ key: e.key }),

  valueEvent: (e) => ({ value: e.target.value }),

  scrollEvent: () => Utils.getScrollPosition(),

  focusBlurEvent: (e) => {
    const target = e.target;
    return {
      boundingBox: Utils.getBoundingBox(target),
      xpath: Utils.getPathTo(target),
    };
  },
};

// Configuration for different event types
const interactionConfig = {
  click: EventHandlers.mouseEvent,
  dblclick: EventHandlers.mouseEvent,
  mousedown: EventHandlers.mouseEvent,
  mouseup: EventHandlers.mouseEvent,
  keydown: EventHandlers.keyEvent,
  keyup: EventHandlers.keyEvent,
  input: EventHandlers.valueEvent,
  change: EventHandlers.valueEvent,
  scroll: EventHandlers.scrollEvent,
  dragstart: EventHandlers.mouseEvent,
  dragend: EventHandlers.mouseEvent,
  drop: EventHandlers.mouseEvent,
  focus: EventHandlers.focusBlurEvent,
  blur: EventHandlers.focusBlurEvent,
};

// Main event handling function
function handleEvent(event) {
  const handler = interactionConfig[event.type];
  if (!handler) return;

  const details = {
    ...handler(event),
    url: window.location.href,
    outer_html: event.target.outerHTML,
  };

  // Only add boundingBox and xpath if not a scroll event
  if (event.type !== 'scroll') {
    details.boundingBox = Utils.getBoundingBox(event.target);
    details.xpath = Utils.getPathTo(event.target);
  }

  // Add scroll position for all events
  details.scroll = Utils.getScrollPosition();

  Utils.sendInteraction(event.type, details);
}

// Special handler for select elements
function handleSelectChange(event) {
  const target = event.target;
  if (target.tagName.toLowerCase() !== 'select') return;

  const details = {
    value: target.value,
    options: Array.from(target.selectedOptions).map(option => option.value),
    target: target.outerHTML,
    boundingBox: Utils.getBoundingBox(target),
    xpath: Utils.getPathTo(target),
    scroll: Utils.getScrollPosition(),
    url: window.location.href,
  };
  Utils.sendInteraction('select', details);
}

// Setup function
function setupEventListeners() {
  Object.keys(interactionConfig).forEach(eventType => {
    const useCapture = ['focus', 'blur'].includes(eventType);
    document.addEventListener(eventType, handleEvent, useCapture);
  });

  document.addEventListener('change', handleSelectChange);
  console.log('Event listeners set up');
}

// Initialize event listeners
setupEventListeners();
