const {
  SvelteComponent: He,
  assign: Re,
  create_slot: Oe,
  detach: Te,
  element: We,
  get_all_dirty_from_scope: De,
  get_slot_changes: Fe,
  get_spread_update: Ge,
  init: Je,
  insert: Ke,
  safe_not_equal: Pe,
  set_dynamic_element_data: ce,
  set_style: j,
  toggle_class: E,
  transition_in: ve,
  transition_out: ye,
  update_slot_base: Qe
} = window.__gradio__svelte__internal;
function Ue(n) {
  let e, l, f;
  const i = (
    /*#slots*/
    n[18].default
  ), o = Oe(
    i,
    n,
    /*$$scope*/
    n[17],
    null
  );
  let c = [
    { "data-testid": (
      /*test_id*/
      n[7]
    ) },
    { id: (
      /*elem_id*/
      n[2]
    ) },
    {
      class: l = "block " + /*elem_classes*/
      n[3].join(" ") + " svelte-1t38q2d"
    }
  ], s = {};
  for (let t = 0; t < c.length; t += 1)
    s = Re(s, c[t]);
  return {
    c() {
      e = We(
        /*tag*/
        n[14]
      ), o && o.c(), ce(
        /*tag*/
        n[14]
      )(e, s), E(
        e,
        "hidden",
        /*visible*/
        n[10] === !1
      ), E(
        e,
        "padded",
        /*padding*/
        n[6]
      ), E(
        e,
        "border_focus",
        /*border_mode*/
        n[5] === "focus"
      ), E(e, "hide-container", !/*explicit_call*/
      n[8] && !/*container*/
      n[9]), j(
        e,
        "height",
        /*get_dimension*/
        n[15](
          /*height*/
          n[0]
        )
      ), j(e, "width", typeof /*width*/
      n[1] == "number" ? `calc(min(${/*width*/
      n[1]}px, 100%))` : (
        /*get_dimension*/
        n[15](
          /*width*/
          n[1]
        )
      )), j(
        e,
        "border-style",
        /*variant*/
        n[4]
      ), j(
        e,
        "overflow",
        /*allow_overflow*/
        n[11] ? "visible" : "hidden"
      ), j(
        e,
        "flex-grow",
        /*scale*/
        n[12]
      ), j(e, "min-width", `calc(min(${/*min_width*/
      n[13]}px, 100%))`), j(e, "border-width", "var(--block-border-width)");
    },
    m(t, a) {
      Ke(t, e, a), o && o.m(e, null), f = !0;
    },
    p(t, a) {
      o && o.p && (!f || a & /*$$scope*/
      131072) && Qe(
        o,
        i,
        t,
        /*$$scope*/
        t[17],
        f ? Fe(
          i,
          /*$$scope*/
          t[17],
          a,
          null
        ) : De(
          /*$$scope*/
          t[17]
        ),
        null
      ), ce(
        /*tag*/
        t[14]
      )(e, s = Ge(c, [
        (!f || a & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          t[7]
        ) },
        (!f || a & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          t[2]
        ) },
        (!f || a & /*elem_classes*/
        8 && l !== (l = "block " + /*elem_classes*/
        t[3].join(" ") + " svelte-1t38q2d")) && { class: l }
      ])), E(
        e,
        "hidden",
        /*visible*/
        t[10] === !1
      ), E(
        e,
        "padded",
        /*padding*/
        t[6]
      ), E(
        e,
        "border_focus",
        /*border_mode*/
        t[5] === "focus"
      ), E(e, "hide-container", !/*explicit_call*/
      t[8] && !/*container*/
      t[9]), a & /*height*/
      1 && j(
        e,
        "height",
        /*get_dimension*/
        t[15](
          /*height*/
          t[0]
        )
      ), a & /*width*/
      2 && j(e, "width", typeof /*width*/
      t[1] == "number" ? `calc(min(${/*width*/
      t[1]}px, 100%))` : (
        /*get_dimension*/
        t[15](
          /*width*/
          t[1]
        )
      )), a & /*variant*/
      16 && j(
        e,
        "border-style",
        /*variant*/
        t[4]
      ), a & /*allow_overflow*/
      2048 && j(
        e,
        "overflow",
        /*allow_overflow*/
        t[11] ? "visible" : "hidden"
      ), a & /*scale*/
      4096 && j(
        e,
        "flex-grow",
        /*scale*/
        t[12]
      ), a & /*min_width*/
      8192 && j(e, "min-width", `calc(min(${/*min_width*/
      t[13]}px, 100%))`);
    },
    i(t) {
      f || (ve(o, t), f = !0);
    },
    o(t) {
      ye(o, t), f = !1;
    },
    d(t) {
      t && Te(e), o && o.d(t);
    }
  };
}
function Ve(n) {
  let e, l = (
    /*tag*/
    n[14] && Ue(n)
  );
  return {
    c() {
      l && l.c();
    },
    m(f, i) {
      l && l.m(f, i), e = !0;
    },
    p(f, [i]) {
      /*tag*/
      f[14] && l.p(f, i);
    },
    i(f) {
      e || (ve(l, f), e = !0);
    },
    o(f) {
      ye(l, f), e = !1;
    },
    d(f) {
      l && l.d(f);
    }
  };
}
function Ze(n, e, l) {
  let { $$slots: f = {}, $$scope: i } = e, { height: o = void 0 } = e, { width: c = void 0 } = e, { elem_id: s = "" } = e, { elem_classes: t = [] } = e, { variant: a = "solid" } = e, { border_mode: _ = "base" } = e, { padding: u = !0 } = e, { type: b = "normal" } = e, { test_id: g = void 0 } = e, { explicit_call: h = !1 } = e, { container: k = !0 } = e, { visible: v = !0 } = e, { allow_overflow: C = !0 } = e, { scale: q = null } = e, { min_width: z = 0 } = e, S = b === "fieldset" ? "fieldset" : "div";
  const M = (r) => {
    if (r !== void 0) {
      if (typeof r == "number")
        return r + "px";
      if (typeof r == "string")
        return r;
    }
  };
  return n.$$set = (r) => {
    "height" in r && l(0, o = r.height), "width" in r && l(1, c = r.width), "elem_id" in r && l(2, s = r.elem_id), "elem_classes" in r && l(3, t = r.elem_classes), "variant" in r && l(4, a = r.variant), "border_mode" in r && l(5, _ = r.border_mode), "padding" in r && l(6, u = r.padding), "type" in r && l(16, b = r.type), "test_id" in r && l(7, g = r.test_id), "explicit_call" in r && l(8, h = r.explicit_call), "container" in r && l(9, k = r.container), "visible" in r && l(10, v = r.visible), "allow_overflow" in r && l(11, C = r.allow_overflow), "scale" in r && l(12, q = r.scale), "min_width" in r && l(13, z = r.min_width), "$$scope" in r && l(17, i = r.$$scope);
  }, [
    o,
    c,
    s,
    t,
    a,
    _,
    u,
    g,
    h,
    k,
    v,
    C,
    q,
    z,
    S,
    M,
    b,
    i,
    f
  ];
}
class pe extends He {
  constructor(e) {
    super(), Je(this, e, Ze, Ve, Pe, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 16,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const xe = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], _e = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
xe.reduce(
  (n, { color: e, primary: l, secondary: f }) => ({
    ...n,
    [e]: {
      primary: _e[e][l],
      secondary: _e[e][f]
    }
  }),
  {}
);
const {
  SvelteComponent: $e,
  attr: K,
  create_slot: el,
  detach: ll,
  element: nl,
  get_all_dirty_from_scope: tl,
  get_slot_changes: il,
  init: fl,
  insert: ol,
  null_to_empty: de,
  safe_not_equal: al,
  set_style: P,
  toggle_class: Y,
  transition_in: sl,
  transition_out: cl,
  update_slot_base: _l
} = window.__gradio__svelte__internal;
function dl(n) {
  let e, l, f = `calc(min(${/*min_width*/
  n[2]}px, 100%))`, i;
  const o = (
    /*#slots*/
    n[8].default
  ), c = el(
    o,
    n,
    /*$$scope*/
    n[7],
    null
  );
  return {
    c() {
      e = nl("div"), c && c.c(), K(
        e,
        "id",
        /*elem_id*/
        n[3]
      ), K(e, "class", l = de(
        /*elem_classes*/
        n[4].join(" ")
      ) + " svelte-1m1obck"), Y(
        e,
        "gap",
        /*gap*/
        n[1]
      ), Y(
        e,
        "compact",
        /*variant*/
        n[6] === "compact"
      ), Y(
        e,
        "panel",
        /*variant*/
        n[6] === "panel"
      ), Y(e, "hide", !/*visible*/
      n[5]), P(
        e,
        "flex-grow",
        /*scale*/
        n[0]
      ), P(e, "min-width", f);
    },
    m(s, t) {
      ol(s, e, t), c && c.m(e, null), i = !0;
    },
    p(s, [t]) {
      c && c.p && (!i || t & /*$$scope*/
      128) && _l(
        c,
        o,
        s,
        /*$$scope*/
        s[7],
        i ? il(
          o,
          /*$$scope*/
          s[7],
          t,
          null
        ) : tl(
          /*$$scope*/
          s[7]
        ),
        null
      ), (!i || t & /*elem_id*/
      8) && K(
        e,
        "id",
        /*elem_id*/
        s[3]
      ), (!i || t & /*elem_classes*/
      16 && l !== (l = de(
        /*elem_classes*/
        s[4].join(" ")
      ) + " svelte-1m1obck")) && K(e, "class", l), (!i || t & /*elem_classes, gap*/
      18) && Y(
        e,
        "gap",
        /*gap*/
        s[1]
      ), (!i || t & /*elem_classes, variant*/
      80) && Y(
        e,
        "compact",
        /*variant*/
        s[6] === "compact"
      ), (!i || t & /*elem_classes, variant*/
      80) && Y(
        e,
        "panel",
        /*variant*/
        s[6] === "panel"
      ), (!i || t & /*elem_classes, visible*/
      48) && Y(e, "hide", !/*visible*/
      s[5]), t & /*scale*/
      1 && P(
        e,
        "flex-grow",
        /*scale*/
        s[0]
      ), t & /*min_width*/
      4 && f !== (f = `calc(min(${/*min_width*/
      s[2]}px, 100%))`) && P(e, "min-width", f);
    },
    i(s) {
      i || (sl(c, s), i = !0);
    },
    o(s) {
      cl(c, s), i = !1;
    },
    d(s) {
      s && ll(e), c && c.d(s);
    }
  };
}
function rl(n, e, l) {
  let { $$slots: f = {}, $$scope: i } = e, { scale: o = null } = e, { gap: c = !0 } = e, { min_width: s = 0 } = e, { elem_id: t = "" } = e, { elem_classes: a = [] } = e, { visible: _ = !0 } = e, { variant: u = "default" } = e;
  return n.$$set = (b) => {
    "scale" in b && l(0, o = b.scale), "gap" in b && l(1, c = b.gap), "min_width" in b && l(2, s = b.min_width), "elem_id" in b && l(3, t = b.elem_id), "elem_classes" in b && l(4, a = b.elem_classes), "visible" in b && l(5, _ = b.visible), "variant" in b && l(6, u = b.variant), "$$scope" in b && l(7, i = b.$$scope);
  }, [o, c, s, t, a, _, u, i, f];
}
let ul = class extends $e {
  constructor(e) {
    super(), fl(this, e, rl, dl, al, {
      scale: 0,
      gap: 1,
      min_width: 2,
      elem_id: 3,
      elem_classes: 4,
      visible: 5,
      variant: 6
    });
  }
};
const {
  SvelteComponent: ml,
  append: je,
  attr: w,
  bubble: bl,
  check_outros: gl,
  create_slot: qe,
  detach: W,
  element: ee,
  empty: hl,
  get_all_dirty_from_scope: ze,
  get_slot_changes: Ce,
  group_outros: wl,
  init: kl,
  insert: D,
  listen: vl,
  safe_not_equal: yl,
  set_style: re,
  space: Se,
  src_url_equal: U,
  toggle_class: O,
  transition_in: V,
  transition_out: Z,
  update_slot_base: Me
} = window.__gradio__svelte__internal;
function jl(n) {
  let e, l, f, i, o, c, s = (
    /*icon*/
    n[7] && ue(n)
  );
  const t = (
    /*#slots*/
    n[19].default
  ), a = qe(
    t,
    n,
    /*$$scope*/
    n[18],
    null
  );
  return {
    c() {
      e = ee("button"), s && s.c(), l = Se(), a && a.c(), w(e, "class", f = /*size*/
      n[4] + " " + /*variant*/
      n[3] + " " + /*elem_classes*/
      n[1].join(" ") + " " + /*class_name*/
      n[9] + " svelte-dq8bxj"), w(
        e,
        "style",
        /*customStyle*/
        n[10]
      ), w(
        e,
        "id",
        /*elem_id*/
        n[0]
      ), e.disabled = /*disabled*/
      n[8], O(e, "hidden", !/*visible*/
      n[2]);
    },
    m(_, u) {
      D(_, e, u), s && s.m(e, null), je(e, l), a && a.m(e, null), i = !0, o || (c = vl(
        e,
        "click",
        /*click_handler*/
        n[20]
      ), o = !0);
    },
    p(_, u) {
      /*icon*/
      _[7] ? s ? s.p(_, u) : (s = ue(_), s.c(), s.m(e, l)) : s && (s.d(1), s = null), a && a.p && (!i || u & /*$$scope*/
      262144) && Me(
        a,
        t,
        _,
        /*$$scope*/
        _[18],
        i ? Ce(
          t,
          /*$$scope*/
          _[18],
          u,
          null
        ) : ze(
          /*$$scope*/
          _[18]
        ),
        null
      ), (!i || u & /*size, variant, elem_classes, class_name*/
      538 && f !== (f = /*size*/
      _[4] + " " + /*variant*/
      _[3] + " " + /*elem_classes*/
      _[1].join(" ") + " " + /*class_name*/
      _[9] + " svelte-dq8bxj")) && w(e, "class", f), (!i || u & /*customStyle*/
      1024) && w(
        e,
        "style",
        /*customStyle*/
        _[10]
      ), (!i || u & /*elem_id*/
      1) && w(
        e,
        "id",
        /*elem_id*/
        _[0]
      ), (!i || u & /*disabled*/
      256) && (e.disabled = /*disabled*/
      _[8]), (!i || u & /*size, variant, elem_classes, class_name, visible*/
      542) && O(e, "hidden", !/*visible*/
      _[2]);
    },
    i(_) {
      i || (V(a, _), i = !0);
    },
    o(_) {
      Z(a, _), i = !1;
    },
    d(_) {
      _ && W(e), s && s.d(), a && a.d(_), o = !1, c();
    }
  };
}
function ql(n) {
  let e, l, f, i, o = (
    /*icon*/
    n[7] && me(n)
  );
  const c = (
    /*#slots*/
    n[19].default
  ), s = qe(
    c,
    n,
    /*$$scope*/
    n[18],
    null
  );
  return {
    c() {
      e = ee("a"), o && o.c(), l = Se(), s && s.c(), w(
        e,
        "href",
        /*link*/
        n[6]
      ), w(e, "rel", "noopener noreferrer"), w(
        e,
        "aria-disabled",
        /*disabled*/
        n[8]
      ), w(e, "class", f = /*size*/
      n[4] + " " + /*variant*/
      n[3] + " " + /*elem_classes*/
      n[1].join(" ") + " svelte-dq8bxj"), w(
        e,
        "style",
        /*customStyle*/
        n[10]
      ), w(
        e,
        "id",
        /*elem_id*/
        n[0]
      ), O(e, "hidden", !/*visible*/
      n[2]), O(
        e,
        "disabled",
        /*disabled*/
        n[8]
      ), re(
        e,
        "pointer-events",
        /*disabled*/
        n[8] ? "none" : null
      );
    },
    m(t, a) {
      D(t, e, a), o && o.m(e, null), je(e, l), s && s.m(e, null), i = !0;
    },
    p(t, a) {
      /*icon*/
      t[7] ? o ? o.p(t, a) : (o = me(t), o.c(), o.m(e, l)) : o && (o.d(1), o = null), s && s.p && (!i || a & /*$$scope*/
      262144) && Me(
        s,
        c,
        t,
        /*$$scope*/
        t[18],
        i ? Ce(
          c,
          /*$$scope*/
          t[18],
          a,
          null
        ) : ze(
          /*$$scope*/
          t[18]
        ),
        null
      ), (!i || a & /*link*/
      64) && w(
        e,
        "href",
        /*link*/
        t[6]
      ), (!i || a & /*disabled*/
      256) && w(
        e,
        "aria-disabled",
        /*disabled*/
        t[8]
      ), (!i || a & /*size, variant, elem_classes*/
      26 && f !== (f = /*size*/
      t[4] + " " + /*variant*/
      t[3] + " " + /*elem_classes*/
      t[1].join(" ") + " svelte-dq8bxj")) && w(e, "class", f), (!i || a & /*customStyle*/
      1024) && w(
        e,
        "style",
        /*customStyle*/
        t[10]
      ), (!i || a & /*elem_id*/
      1) && w(
        e,
        "id",
        /*elem_id*/
        t[0]
      ), (!i || a & /*size, variant, elem_classes, visible*/
      30) && O(e, "hidden", !/*visible*/
      t[2]), (!i || a & /*size, variant, elem_classes, disabled*/
      282) && O(
        e,
        "disabled",
        /*disabled*/
        t[8]
      );
      const _ = a & /*customStyle*/
      1024;
      (a & /*disabled, customStyle*/
      1280 || _) && re(
        e,
        "pointer-events",
        /*disabled*/
        t[8] ? "none" : null
      );
    },
    i(t) {
      i || (V(s, t), i = !0);
    },
    o(t) {
      Z(s, t), i = !1;
    },
    d(t) {
      t && W(e), o && o.d(), s && s.d(t);
    }
  };
}
function ue(n) {
  let e, l, f;
  return {
    c() {
      e = ee("img"), w(e, "class", "button-icon svelte-dq8bxj"), U(e.src, l = /*icon*/
      n[7].url) || w(e, "src", l), w(e, "alt", f = `${/*value*/
      n[5]} icon`);
    },
    m(i, o) {
      D(i, e, o);
    },
    p(i, o) {
      o & /*icon*/
      128 && !U(e.src, l = /*icon*/
      i[7].url) && w(e, "src", l), o & /*value*/
      32 && f !== (f = `${/*value*/
      i[5]} icon`) && w(e, "alt", f);
    },
    d(i) {
      i && W(e);
    }
  };
}
function me(n) {
  let e, l, f;
  return {
    c() {
      e = ee("img"), w(e, "class", "button-icon svelte-dq8bxj"), U(e.src, l = /*icon*/
      n[7].url) || w(e, "src", l), w(e, "alt", f = `${/*value*/
      n[5]} icon`);
    },
    m(i, o) {
      D(i, e, o);
    },
    p(i, o) {
      o & /*icon*/
      128 && !U(e.src, l = /*icon*/
      i[7].url) && w(e, "src", l), o & /*value*/
      32 && f !== (f = `${/*value*/
      i[5]} icon`) && w(e, "alt", f);
    },
    d(i) {
      i && W(e);
    }
  };
}
function zl(n) {
  let e, l, f, i;
  const o = [ql, jl], c = [];
  function s(t, a) {
    return (
      /*link*/
      t[6] && /*link*/
      t[6].length > 0 ? 0 : 1
    );
  }
  return e = s(n), l = c[e] = o[e](n), {
    c() {
      l.c(), f = hl();
    },
    m(t, a) {
      c[e].m(t, a), D(t, f, a), i = !0;
    },
    p(t, [a]) {
      let _ = e;
      e = s(t), e === _ ? c[e].p(t, a) : (wl(), Z(c[_], 1, 1, () => {
        c[_] = null;
      }), gl(), l = c[e], l ? l.p(t, a) : (l = c[e] = o[e](t), l.c()), V(l, 1), l.m(f.parentNode, f));
    },
    i(t) {
      i || (V(l), i = !0);
    },
    o(t) {
      Z(l), i = !1;
    },
    d(t) {
      t && W(f), c[e].d(t);
    }
  };
}
function Cl(n, e, l) {
  let f, { $$slots: i = {}, $$scope: o } = e, { elem_id: c = "" } = e, { elem_classes: s = [] } = e, { visible: t = !0 } = e, { variant: a = "secondary" } = e, { size: _ = "lg" } = e, { value: u = null } = e, { link: b = null } = e, { icon: g = null } = e, { disabled: h = !1 } = e, { scale: k = null } = e, { class_name: v = null } = e, { background_color: C = null } = e, { color: q = null } = e, { border_color: z = null } = e, { height: S = null } = e, { width: M = null } = e, { min_width: r = void 0 } = e;
  function H(m) {
    bl.call(this, n, m);
  }
  return n.$$set = (m) => {
    "elem_id" in m && l(0, c = m.elem_id), "elem_classes" in m && l(1, s = m.elem_classes), "visible" in m && l(2, t = m.visible), "variant" in m && l(3, a = m.variant), "size" in m && l(4, _ = m.size), "value" in m && l(5, u = m.value), "link" in m && l(6, b = m.link), "icon" in m && l(7, g = m.icon), "disabled" in m && l(8, h = m.disabled), "scale" in m && l(11, k = m.scale), "class_name" in m && l(9, v = m.class_name), "background_color" in m && l(12, C = m.background_color), "color" in m && l(13, q = m.color), "border_color" in m && l(14, z = m.border_color), "height" in m && l(15, S = m.height), "width" in m && l(16, M = m.width), "min_width" in m && l(17, r = m.min_width), "$$scope" in m && l(18, o = m.$$scope);
  }, n.$$.update = () => {
    n.$$.dirty & /*height, width, border_color, background_color, color, scale, min_width*/
    260096 && l(10, f = `
		${S ? `height: ${S};` : ""}
		${M ? `width: ${M};` : ""}
		${z ? `border-color: ${z} !important;` : ""}
		${C ? `background: ${C} !important;` : ""}
		${q ? `color: ${q} !important;` : ""}
		${k !== null ? `flex-grow: ${k};` : ""}
		${k === 0 ? "width: fit-content;" : ""}
		${typeof r == "number" ? `min-width: calc(min(${r}px, 100%));` : ""}
	`);
  }, [
    c,
    s,
    t,
    a,
    _,
    u,
    b,
    g,
    h,
    v,
    f,
    k,
    C,
    q,
    z,
    S,
    M,
    r,
    o,
    i,
    H
  ];
}
class be extends ml {
  constructor(e) {
    super(), kl(this, e, Cl, zl, yl, {
      elem_id: 0,
      elem_classes: 1,
      visible: 2,
      variant: 3,
      size: 4,
      value: 5,
      link: 6,
      icon: 7,
      disabled: 8,
      scale: 11,
      class_name: 9,
      background_color: 12,
      color: 13,
      border_color: 14,
      height: 15,
      width: 16,
      min_width: 17
    });
  }
}
const {
  SvelteComponent: Sl,
  append: L,
  attr: y,
  binding_callbacks: ge,
  check_outros: Ml,
  create_component: p,
  create_slot: Ll,
  destroy_component: x,
  detach: X,
  element: B,
  get_all_dirty_from_scope: Bl,
  get_slot_changes: El,
  group_outros: Yl,
  init: Il,
  insert: A,
  listen: Le,
  mount_component: $,
  noop: Nl,
  safe_not_equal: Xl,
  set_data: ne,
  set_style: Q,
  space: T,
  text: te,
  toggle_class: he,
  transition_in: I,
  transition_out: N,
  update_slot_base: Al
} = window.__gradio__svelte__internal, { onMount: Hl } = window.__gradio__svelte__internal;
function we(n) {
  let e, l, f;
  return {
    c() {
      e = B("div"), e.innerHTML = '<svg width="10" height="10" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1 1L9 9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 1L1 9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>', y(e, "class", "close svelte-8dp453");
    },
    m(i, o) {
      A(i, e, o), l || (f = Le(
        e,
        "click",
        /*close*/
        n[14]
      ), l = !0);
    },
    p: Nl,
    d(i) {
      i && X(e), l = !1, f();
    }
  };
}
function Rl(n) {
  let e;
  const l = (
    /*#slots*/
    n[28].default
  ), f = Ll(
    l,
    n,
    /*$$scope*/
    n[32],
    null
  );
  return {
    c() {
      f && f.c();
    },
    m(i, o) {
      f && f.m(i, o), e = !0;
    },
    p(i, o) {
      f && f.p && (!e || o[1] & /*$$scope*/
      2) && Al(
        f,
        l,
        i,
        /*$$scope*/
        i[32],
        e ? El(
          l,
          /*$$scope*/
          i[32],
          o,
          null
        ) : Bl(
          /*$$scope*/
          i[32]
        ),
        null
      );
    },
    i(i) {
      e || (I(f, i), e = !0);
    },
    o(i) {
      N(f, i), e = !1;
    },
    d(i) {
      f && f.d(i);
    }
  };
}
function Ol(n) {
  let e, l, f, i, o = (
    /*display_close_icon*/
    n[3] && we(n)
  );
  return f = new ul({
    props: {
      elem_classes: ["centered-column"],
      $$slots: { default: [Rl] },
      $$scope: { ctx: n }
    }
  }), {
    c() {
      o && o.c(), e = T(), l = B("div"), p(f.$$.fragment), y(l, "class", "modal-content svelte-8dp453"), y(
        l,
        "style",
        /*contentStyle*/
        n[10]
      );
    },
    m(c, s) {
      o && o.m(c, s), A(c, e, s), A(c, l, s), $(f, l, null), i = !0;
    },
    p(c, s) {
      /*display_close_icon*/
      c[3] ? o ? o.p(c, s) : (o = we(c), o.c(), o.m(e.parentNode, e)) : o && (o.d(1), o = null);
      const t = {};
      s[1] & /*$$scope*/
      2 && (t.$$scope = { dirty: s, ctx: c }), f.$set(t), (!i || s[0] & /*contentStyle*/
      1024) && y(
        l,
        "style",
        /*contentStyle*/
        c[10]
      );
    },
    i(c) {
      i || (I(f.$$.fragment, c), i = !0);
    },
    o(c) {
      N(f.$$.fragment, c), i = !1;
    },
    d(c) {
      c && (X(e), X(l)), o && o.d(c), x(f);
    }
  };
}
function ke(n) {
  let e, l, f, i, o, c, s, t, a, _, u, b;
  return a = new be({
    props: {
      class_name: "no-button",
      background_color: (
        /*close_message_style*/
        n[6].cancel_bg_color
      ),
      color: (
        /*close_message_style*/
        n[6].cancel_text_color
      ),
      border_color: (
        /*close_message_style*/
        n[6].cancel_border_color
      ),
      width: (
        /*close_message_style*/
        n[6].width
      ),
      height: (
        /*close_message_style*/
        n[6].height
      ),
      size: (
        /*close_message_style*/
        n[6].size
      ),
      $$slots: { default: [Tl] },
      $$scope: { ctx: n }
    }
  }), a.$on(
    "click",
    /*cancelClose*/
    n[16]
  ), u = new be({
    props: {
      class_name: "yes-button",
      background_color: (
        /*close_message_style*/
        n[6].confirm_bg_color
      ),
      color: (
        /*close_message_style*/
        n[6].confirm_text_color
      ),
      border_color: (
        /*close_message_style*/
        n[6].confirm_border_color
      ),
      width: (
        /*close_message_style*/
        n[6].width
      ),
      height: (
        /*close_message_style*/
        n[6].height
      ),
      size: (
        /*close_message_style*/
        n[6].size
      ),
      $$slots: { default: [Wl] },
      $$scope: { ctx: n }
    }
  }), u.$on(
    "click",
    /*closeModal*/
    n[15]
  ), {
    c() {
      e = B("div"), l = B("div"), f = B("h3"), i = te(
        /*close_message*/
        n[5]
      ), o = T(), c = B("br"), s = T(), t = B("div"), p(a.$$.fragment), _ = T(), p(u.$$.fragment), Q(
        f,
        "color",
        /*close_message_style*/
        n[6].message_color
      ), y(f, "class", "svelte-8dp453"), y(t, "class", "confirmation-buttons svelte-8dp453"), y(l, "class", "confirmation-content svelte-8dp453"), Q(
        l,
        "background-color",
        /*close_message_style*/
        n[6].modal_bg_color
      ), y(e, "class", "confirmation-modal svelte-8dp453");
    },
    m(g, h) {
      A(g, e, h), L(e, l), L(l, f), L(f, i), L(l, o), L(l, c), L(l, s), L(l, t), $(a, t, null), L(t, _), $(u, t, null), b = !0;
    },
    p(g, h) {
      (!b || h[0] & /*close_message*/
      32) && ne(
        i,
        /*close_message*/
        g[5]
      ), (!b || h[0] & /*close_message_style*/
      64) && Q(
        f,
        "color",
        /*close_message_style*/
        g[6].message_color
      );
      const k = {};
      h[0] & /*close_message_style*/
      64 && (k.background_color = /*close_message_style*/
      g[6].cancel_bg_color), h[0] & /*close_message_style*/
      64 && (k.color = /*close_message_style*/
      g[6].cancel_text_color), h[0] & /*close_message_style*/
      64 && (k.border_color = /*close_message_style*/
      g[6].cancel_border_color), h[0] & /*close_message_style*/
      64 && (k.width = /*close_message_style*/
      g[6].width), h[0] & /*close_message_style*/
      64 && (k.height = /*close_message_style*/
      g[6].height), h[0] & /*close_message_style*/
      64 && (k.size = /*close_message_style*/
      g[6].size), h[0] & /*close_message_style*/
      64 | h[1] & /*$$scope*/
      2 && (k.$$scope = { dirty: h, ctx: g }), a.$set(k);
      const v = {};
      h[0] & /*close_message_style*/
      64 && (v.background_color = /*close_message_style*/
      g[6].confirm_bg_color), h[0] & /*close_message_style*/
      64 && (v.color = /*close_message_style*/
      g[6].confirm_text_color), h[0] & /*close_message_style*/
      64 && (v.border_color = /*close_message_style*/
      g[6].confirm_border_color), h[0] & /*close_message_style*/
      64 && (v.width = /*close_message_style*/
      g[6].width), h[0] & /*close_message_style*/
      64 && (v.height = /*close_message_style*/
      g[6].height), h[0] & /*close_message_style*/
      64 && (v.size = /*close_message_style*/
      g[6].size), h[0] & /*close_message_style*/
      64 | h[1] & /*$$scope*/
      2 && (v.$$scope = { dirty: h, ctx: g }), u.$set(v), (!b || h[0] & /*close_message_style*/
      64) && Q(
        l,
        "background-color",
        /*close_message_style*/
        g[6].modal_bg_color
      );
    },
    i(g) {
      b || (I(a.$$.fragment, g), I(u.$$.fragment, g), b = !0);
    },
    o(g) {
      N(a.$$.fragment, g), N(u.$$.fragment, g), b = !1;
    },
    d(g) {
      g && X(e), x(a), x(u);
    }
  };
}
function Tl(n) {
  let e = (
    /*close_message_style*/
    n[6].cancel_text + ""
  ), l;
  return {
    c() {
      l = te(e);
    },
    m(f, i) {
      A(f, l, i);
    },
    p(f, i) {
      i[0] & /*close_message_style*/
      64 && e !== (e = /*close_message_style*/
      f[6].cancel_text + "") && ne(l, e);
    },
    d(f) {
      f && X(l);
    }
  };
}
function Wl(n) {
  let e = (
    /*close_message_style*/
    n[6].confirm_text + ""
  ), l;
  return {
    c() {
      l = te(e);
    },
    m(f, i) {
      A(f, l, i);
    },
    p(f, i) {
      i[0] & /*close_message_style*/
      64 && e !== (e = /*close_message_style*/
      f[6].confirm_text + "") && ne(l, e);
    },
    d(f) {
      f && X(l);
    }
  };
}
function Dl(n) {
  let e, l, f, i, o, c, s, t;
  f = new pe({
    props: {
      allow_overflow: !1,
      elem_classes: ["modal-block"],
      $$slots: { default: [Ol] },
      $$scope: { ctx: n }
    }
  });
  let a = (
    /*showConfirmation*/
    n[9] && ke(n)
  );
  return {
    c() {
      e = B("div"), l = B("div"), p(f.$$.fragment), i = T(), a && a.c(), y(l, "class", "modal-container svelte-8dp453"), y(
        l,
        "style",
        /*containerStyle*/
        n[11]
      ), y(e, "class", o = "modal " + /*elem_classes*/
      n[2].join(" ") + " " + /*getAnimationClass*/
      n[13]() + " svelte-8dp453"), y(
        e,
        "id",
        /*elem_id*/
        n[1]
      ), y(
        e,
        "style",
        /*modalStyle*/
        n[12]
      ), he(e, "hide", !/*visible*/
      n[0]);
    },
    m(_, u) {
      A(_, e, u), L(e, l), $(f, l, null), n[29](l), L(e, i), a && a.m(e, null), n[30](e), c = !0, s || (t = Le(
        e,
        "click",
        /*click_handler*/
        n[31]
      ), s = !0);
    },
    p(_, u) {
      const b = {};
      u[0] & /*contentStyle, display_close_icon*/
      1032 | u[1] & /*$$scope*/
      2 && (b.$$scope = { dirty: u, ctx: _ }), f.$set(b), (!c || u[0] & /*containerStyle*/
      2048) && y(
        l,
        "style",
        /*containerStyle*/
        _[11]
      ), /*showConfirmation*/
      _[9] ? a ? (a.p(_, u), u[0] & /*showConfirmation*/
      512 && I(a, 1)) : (a = ke(_), a.c(), I(a, 1), a.m(e, null)) : a && (Yl(), N(a, 1, 1, () => {
        a = null;
      }), Ml()), (!c || u[0] & /*elem_classes*/
      4 && o !== (o = "modal " + /*elem_classes*/
      _[2].join(" ") + " " + /*getAnimationClass*/
      _[13]() + " svelte-8dp453")) && y(e, "class", o), (!c || u[0] & /*elem_id*/
      2) && y(
        e,
        "id",
        /*elem_id*/
        _[1]
      ), (!c || u[0] & /*modalStyle*/
      4096) && y(
        e,
        "style",
        /*modalStyle*/
        _[12]
      ), (!c || u[0] & /*elem_classes, visible*/
      5) && he(e, "hide", !/*visible*/
      _[0]);
    },
    i(_) {
      c || (I(f.$$.fragment, _), I(a), c = !0);
    },
    o(_) {
      N(f.$$.fragment, _), N(a), c = !1;
    },
    d(_) {
      _ && X(e), x(f), n[29](null), a && a.d(), n[30](null), s = !1, t();
    }
  };
}
function Fl(n, e, l) {
  let f, i, o, { $$slots: c = {}, $$scope: s } = e, { elem_id: t = "" } = e, { elem_classes: a = [] } = e, { visible: _ = !1 } = e, { display_close_icon: u = !1 } = e, { close_on_esc: b } = e, { close_outer_click: g } = e, { close_message: h } = e, { bg_blur: k } = e, { width: v } = e, { height: C } = e, { content_width_percent: q } = e, { content_height_percent: z } = e, { content_padding: S } = e, { opacity_level: M } = e, { animate: r } = e, { animation_duration: H = 0.4 } = e, { gradio: m } = e, { close_message_style: ie = {
    message_color: "var(--body-text-color)",
    confirm_text: "Yes",
    cancel_text: "No",
    confirm_bg_color: "var(--primary-500)",
    cancel_bg_color: "var(--neutral-500)",
    confirm_text_color: "white",
    cancel_text_color: "white",
    modal_bg_color: "var(--background-fill-primary)"
  } } = e, F = null, R = null, G = !1, fe = 0, oe = 0, ae = null;
  Hl(() => {
    document.addEventListener("click", (d) => {
      _ || (fe = d.clientX, oe = d.clientY);
    });
  });
  function Be() {
    if (!r) return "";
    switch (r.toLowerCase()) {
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
  function Ee() {
    if (!ae) return "";
    const d = Math.max(0, Math.min(fe, window.innerWidth)), le = Math.max(0, Math.min(oe, window.innerHeight));
    return `transform-origin: ${d}px ${le}px;`;
  }
  const J = () => {
    h ? l(9, G = !0) : se();
  }, se = () => {
    l(0, _ = !1), l(9, G = !1), m.dispatch("blur");
  }, Ye = () => {
    l(9, G = !1);
  };
  document.addEventListener("keydown", (d) => {
    b && d.key === "Escape" && J();
  }), document.addEventListener("keydown", (d) => {
    b && d.key === "Escape" && J();
  });
  function Ie(d) {
    ge[d ? "unshift" : "push"](() => {
      R = d, l(7, R);
    });
  }
  function Ne(d) {
    ge[d ? "unshift" : "push"](() => {
      F = d, l(8, F);
    });
  }
  const Xe = (d) => {
    g && (d.target === F || d.target === R) && J();
  };
  return n.$$set = (d) => {
    "elem_id" in d && l(1, t = d.elem_id), "elem_classes" in d && l(2, a = d.elem_classes), "visible" in d && l(0, _ = d.visible), "display_close_icon" in d && l(3, u = d.display_close_icon), "close_on_esc" in d && l(17, b = d.close_on_esc), "close_outer_click" in d && l(4, g = d.close_outer_click), "close_message" in d && l(5, h = d.close_message), "bg_blur" in d && l(18, k = d.bg_blur), "width" in d && l(19, v = d.width), "height" in d && l(20, C = d.height), "content_width_percent" in d && l(21, q = d.content_width_percent), "content_height_percent" in d && l(22, z = d.content_height_percent), "content_padding" in d && l(23, S = d.content_padding), "opacity_level" in d && l(24, M = d.opacity_level), "animate" in d && l(25, r = d.animate), "animation_duration" in d && l(26, H = d.animation_duration), "gradio" in d && l(27, m = d.gradio), "close_message_style" in d && l(6, ie = d.close_message_style), "$$scope" in d && l(32, s = d.$$scope);
  }, n.$$.update = () => {
    n.$$.dirty[0] & /*inner_element*/
    128 && R && (ae = R.getBoundingClientRect()), n.$$.dirty[0] & /*bg_blur, opacity_level, animation_duration*/
    84148224 && l(12, f = `
    backdrop-filter: blur(${k}px);
    -webkit-backdrop-filter: blur(${k}px);
    background-color: rgba(0, 0, 0, ${M});
    --animation-duration: ${H}s;
  `), n.$$.dirty[0] & /*width, height, animation_duration*/
    68681728 && l(11, i = `
    width: ${v}px;
    height: ${C}px;
    animation-duration: ${H}s;
    ${Ee()}
  `), n.$$.dirty[0] & /*content_padding, content_width_percent, content_height_percent*/
    14680064 && l(10, o = (() => {
      const d = S ? `${S}` : "0px", le = q ? `${q}%` : "100%", Ae = z ? `${z}%` : "100%";
      return `width: ${le}; max-height: ${Ae}; padding: ${d};`;
    })()), n.$$.dirty[0] & /*bg_blur, opacity_level*/
    17039360 && (console.log("bg_blue", k), console.log("opacity_level", M));
  }, [
    _,
    t,
    a,
    u,
    g,
    h,
    ie,
    R,
    F,
    G,
    o,
    i,
    f,
    Be,
    J,
    se,
    Ye,
    b,
    k,
    v,
    C,
    q,
    z,
    S,
    M,
    r,
    H,
    m,
    c,
    Ie,
    Ne,
    Xe,
    s
  ];
}
class Jl extends Sl {
  constructor(e) {
    super(), Il(
      this,
      e,
      Fl,
      Dl,
      Xl,
      {
        elem_id: 1,
        elem_classes: 2,
        visible: 0,
        display_close_icon: 3,
        close_on_esc: 17,
        close_outer_click: 4,
        close_message: 5,
        bg_blur: 18,
        width: 19,
        height: 20,
        content_width_percent: 21,
        content_height_percent: 22,
        content_padding: 23,
        opacity_level: 24,
        animate: 25,
        animation_duration: 26,
        gradio: 27,
        close_message_style: 6
      },
      null,
      [-1, -1]
    );
  }
}
export {
  be as BaseButton,
  Jl as default
};
