const {
  SvelteComponent: ke,
  append: _e,
  attr: b,
  bubble: ze,
  check_outros: Ce,
  create_slot: se,
  detach: Z,
  element: ee,
  empty: qe,
  get_all_dirty_from_scope: oe,
  get_slot_changes: ce,
  group_outros: Le,
  init: Se,
  insert: P,
  listen: ye,
  safe_not_equal: Ie,
  set_style: k,
  space: de,
  src_url_equal: p,
  toggle_class: G,
  transition_in: x,
  transition_out: $,
  update_slot_base: re
} = window.__gradio__svelte__internal;
function We(l) {
  let e, i, n, t, f, r, u = (
    /*icon*/
    l[7] && ne(l)
  );
  const a = (
    /*#slots*/
    l[12].default
  ), s = se(
    a,
    l,
    /*$$scope*/
    l[11],
    null
  );
  return {
    c() {
      e = ee("button"), u && u.c(), i = de(), s && s.c(), b(e, "class", n = /*size*/
      l[4] + " " + /*variant*/
      l[3] + " " + /*elem_classes*/
      l[1].join(" ") + " svelte-8huxfn"), b(
        e,
        "id",
        /*elem_id*/
        l[0]
      ), e.disabled = /*disabled*/
      l[8], G(e, "hidden", !/*visible*/
      l[2]), k(
        e,
        "flex-grow",
        /*scale*/
        l[9]
      ), k(
        e,
        "width",
        /*scale*/
        l[9] === 0 ? "fit-content" : null
      ), k(e, "min-width", typeof /*min_width*/
      l[10] == "number" ? `calc(min(${/*min_width*/
      l[10]}px, 100%))` : null);
    },
    m(c, o) {
      P(c, e, o), u && u.m(e, null), _e(e, i), s && s.m(e, null), t = !0, f || (r = ye(
        e,
        "click",
        /*click_handler*/
        l[13]
      ), f = !0);
    },
    p(c, o) {
      /*icon*/
      c[7] ? u ? u.p(c, o) : (u = ne(c), u.c(), u.m(e, i)) : u && (u.d(1), u = null), s && s.p && (!t || o & /*$$scope*/
      2048) && re(
        s,
        a,
        c,
        /*$$scope*/
        c[11],
        t ? ce(
          a,
          /*$$scope*/
          c[11],
          o,
          null
        ) : oe(
          /*$$scope*/
          c[11]
        ),
        null
      ), (!t || o & /*size, variant, elem_classes*/
      26 && n !== (n = /*size*/
      c[4] + " " + /*variant*/
      c[3] + " " + /*elem_classes*/
      c[1].join(" ") + " svelte-8huxfn")) && b(e, "class", n), (!t || o & /*elem_id*/
      1) && b(
        e,
        "id",
        /*elem_id*/
        c[0]
      ), (!t || o & /*disabled*/
      256) && (e.disabled = /*disabled*/
      c[8]), (!t || o & /*size, variant, elem_classes, visible*/
      30) && G(e, "hidden", !/*visible*/
      c[2]), o & /*scale*/
      512 && k(
        e,
        "flex-grow",
        /*scale*/
        c[9]
      ), o & /*scale*/
      512 && k(
        e,
        "width",
        /*scale*/
        c[9] === 0 ? "fit-content" : null
      ), o & /*min_width*/
      1024 && k(e, "min-width", typeof /*min_width*/
      c[10] == "number" ? `calc(min(${/*min_width*/
      c[10]}px, 100%))` : null);
    },
    i(c) {
      t || (x(s, c), t = !0);
    },
    o(c) {
      $(s, c), t = !1;
    },
    d(c) {
      c && Z(e), u && u.d(), s && s.d(c), f = !1, r();
    }
  };
}
function Be(l) {
  let e, i, n, t, f = (
    /*icon*/
    l[7] && te(l)
  );
  const r = (
    /*#slots*/
    l[12].default
  ), u = se(
    r,
    l,
    /*$$scope*/
    l[11],
    null
  );
  return {
    c() {
      e = ee("a"), f && f.c(), i = de(), u && u.c(), b(
        e,
        "href",
        /*link*/
        l[6]
      ), b(e, "rel", "noopener noreferrer"), b(
        e,
        "aria-disabled",
        /*disabled*/
        l[8]
      ), b(e, "class", n = /*size*/
      l[4] + " " + /*variant*/
      l[3] + " " + /*elem_classes*/
      l[1].join(" ") + " svelte-8huxfn"), b(
        e,
        "id",
        /*elem_id*/
        l[0]
      ), G(e, "hidden", !/*visible*/
      l[2]), G(
        e,
        "disabled",
        /*disabled*/
        l[8]
      ), k(
        e,
        "flex-grow",
        /*scale*/
        l[9]
      ), k(
        e,
        "pointer-events",
        /*disabled*/
        l[8] ? "none" : null
      ), k(
        e,
        "width",
        /*scale*/
        l[9] === 0 ? "fit-content" : null
      ), k(e, "min-width", typeof /*min_width*/
      l[10] == "number" ? `calc(min(${/*min_width*/
      l[10]}px, 100%))` : null);
    },
    m(a, s) {
      P(a, e, s), f && f.m(e, null), _e(e, i), u && u.m(e, null), t = !0;
    },
    p(a, s) {
      /*icon*/
      a[7] ? f ? f.p(a, s) : (f = te(a), f.c(), f.m(e, i)) : f && (f.d(1), f = null), u && u.p && (!t || s & /*$$scope*/
      2048) && re(
        u,
        r,
        a,
        /*$$scope*/
        a[11],
        t ? ce(
          r,
          /*$$scope*/
          a[11],
          s,
          null
        ) : oe(
          /*$$scope*/
          a[11]
        ),
        null
      ), (!t || s & /*link*/
      64) && b(
        e,
        "href",
        /*link*/
        a[6]
      ), (!t || s & /*disabled*/
      256) && b(
        e,
        "aria-disabled",
        /*disabled*/
        a[8]
      ), (!t || s & /*size, variant, elem_classes*/
      26 && n !== (n = /*size*/
      a[4] + " " + /*variant*/
      a[3] + " " + /*elem_classes*/
      a[1].join(" ") + " svelte-8huxfn")) && b(e, "class", n), (!t || s & /*elem_id*/
      1) && b(
        e,
        "id",
        /*elem_id*/
        a[0]
      ), (!t || s & /*size, variant, elem_classes, visible*/
      30) && G(e, "hidden", !/*visible*/
      a[2]), (!t || s & /*size, variant, elem_classes, disabled*/
      282) && G(
        e,
        "disabled",
        /*disabled*/
        a[8]
      ), s & /*scale*/
      512 && k(
        e,
        "flex-grow",
        /*scale*/
        a[9]
      ), s & /*disabled*/
      256 && k(
        e,
        "pointer-events",
        /*disabled*/
        a[8] ? "none" : null
      ), s & /*scale*/
      512 && k(
        e,
        "width",
        /*scale*/
        a[9] === 0 ? "fit-content" : null
      ), s & /*min_width*/
      1024 && k(e, "min-width", typeof /*min_width*/
      a[10] == "number" ? `calc(min(${/*min_width*/
      a[10]}px, 100%))` : null);
    },
    i(a) {
      t || (x(u, a), t = !0);
    },
    o(a) {
      $(u, a), t = !1;
    },
    d(a) {
      a && Z(e), f && f.d(), u && u.d(a);
    }
  };
}
function ne(l) {
  let e, i, n;
  return {
    c() {
      e = ee("img"), b(e, "class", "button-icon svelte-8huxfn"), p(e.src, i = /*icon*/
      l[7].url) || b(e, "src", i), b(e, "alt", n = `${/*value*/
      l[5]} icon`);
    },
    m(t, f) {
      P(t, e, f);
    },
    p(t, f) {
      f & /*icon*/
      128 && !p(e.src, i = /*icon*/
      t[7].url) && b(e, "src", i), f & /*value*/
      32 && n !== (n = `${/*value*/
      t[5]} icon`) && b(e, "alt", n);
    },
    d(t) {
      t && Z(e);
    }
  };
}
function te(l) {
  let e, i, n;
  return {
    c() {
      e = ee("img"), b(e, "class", "button-icon svelte-8huxfn"), p(e.src, i = /*icon*/
      l[7].url) || b(e, "src", i), b(e, "alt", n = `${/*value*/
      l[5]} icon`);
    },
    m(t, f) {
      P(t, e, f);
    },
    p(t, f) {
      f & /*icon*/
      128 && !p(e.src, i = /*icon*/
      t[7].url) && b(e, "src", i), f & /*value*/
      32 && n !== (n = `${/*value*/
      t[5]} icon`) && b(e, "alt", n);
    },
    d(t) {
      t && Z(e);
    }
  };
}
function Te(l) {
  let e, i, n, t;
  const f = [Be, We], r = [];
  function u(a, s) {
    return (
      /*link*/
      a[6] && /*link*/
      a[6].length > 0 ? 0 : 1
    );
  }
  return e = u(l), i = r[e] = f[e](l), {
    c() {
      i.c(), n = qe();
    },
    m(a, s) {
      r[e].m(a, s), P(a, n, s), t = !0;
    },
    p(a, [s]) {
      let c = e;
      e = u(a), e === c ? r[e].p(a, s) : (Le(), $(r[c], 1, 1, () => {
        r[c] = null;
      }), Ce(), i = r[e], i ? i.p(a, s) : (i = r[e] = f[e](a), i.c()), x(i, 1), i.m(n.parentNode, n));
    },
    i(a) {
      t || (x(i), t = !0);
    },
    o(a) {
      $(i), t = !1;
    },
    d(a) {
      a && Z(n), r[e].d(a);
    }
  };
}
function De(l, e, i) {
  let { $$slots: n = {}, $$scope: t } = e, { elem_id: f = "" } = e, { elem_classes: r = [] } = e, { visible: u = !0 } = e, { variant: a = "secondary" } = e, { size: s = "lg" } = e, { value: c = null } = e, { link: o = null } = e, { icon: h = null } = e, { disabled: g = !1 } = e, { scale: C = null } = e, { min_width: S = void 0 } = e;
  function D(m) {
    ze.call(this, l, m);
  }
  return l.$$set = (m) => {
    "elem_id" in m && i(0, f = m.elem_id), "elem_classes" in m && i(1, r = m.elem_classes), "visible" in m && i(2, u = m.visible), "variant" in m && i(3, a = m.variant), "size" in m && i(4, s = m.size), "value" in m && i(5, c = m.value), "link" in m && i(6, o = m.link), "icon" in m && i(7, h = m.icon), "disabled" in m && i(8, g = m.disabled), "scale" in m && i(9, C = m.scale), "min_width" in m && i(10, S = m.min_width), "$$scope" in m && i(11, t = m.$$scope);
  }, [
    f,
    r,
    u,
    a,
    s,
    c,
    o,
    h,
    g,
    C,
    S,
    t,
    n,
    D
  ];
}
class Ee extends ke {
  constructor(e) {
    super(), Se(this, e, De, Te, Ie, {
      elem_id: 0,
      elem_classes: 1,
      visible: 2,
      variant: 3,
      size: 4,
      value: 5,
      link: 6,
      icon: 7,
      disabled: 8,
      scale: 9,
      min_width: 10
    });
  }
}
var Fe = Object.defineProperty, Ne = (l, e, i) => e in l ? Fe(l, e, { enumerable: !0, configurable: !0, writable: !0, value: i }) : l[e] = i, I = (l, e, i) => (Ne(l, typeof e != "symbol" ? e + "" : e, i), i), me = (l, e, i) => {
  if (!e.has(l))
    throw TypeError("Cannot " + i);
}, V = (l, e, i) => (me(l, e, "read from private field"), i ? i.call(l) : e.get(l)), Oe = (l, e, i) => {
  if (e.has(l))
    throw TypeError("Cannot add the same private member more than once");
  e instanceof WeakSet ? e.add(l) : e.set(l, i);
}, Re = (l, e, i, n) => (me(l, e, "write to private field"), e.set(l, i), i), T;
new Intl.Collator(0, { numeric: 1 }).compare;
async function Ae(l, e) {
  return l.map(
    (i) => new Ue({
      path: i.name,
      orig_name: i.name,
      blob: i,
      size: i.size,
      mime_type: i.type,
      is_stream: e
    })
  );
}
class Ue {
  constructor({
    path: e,
    url: i,
    orig_name: n,
    size: t,
    blob: f,
    is_stream: r,
    mime_type: u,
    alt_text: a
  }) {
    I(this, "path"), I(this, "url"), I(this, "orig_name"), I(this, "size"), I(this, "blob"), I(this, "is_stream"), I(this, "mime_type"), I(this, "alt_text"), I(this, "meta", { _type: "gradio.FileData" }), this.path = e, this.url = i, this.orig_name = n, this.size = t, this.blob = i ? void 0 : f, this.is_stream = r, this.mime_type = u, this.alt_text = a;
  }
}
typeof process < "u" && process.versions && process.versions.node;
class Ci extends TransformStream {
  /** Constructs a new instance. */
  constructor(e = { allowCR: !1 }) {
    super({
      transform: (i, n) => {
        for (i = V(this, T) + i; ; ) {
          const t = i.indexOf(`
`), f = e.allowCR ? i.indexOf("\r") : -1;
          if (f !== -1 && f !== i.length - 1 && (t === -1 || t - 1 > f)) {
            n.enqueue(i.slice(0, f)), i = i.slice(f + 1);
            continue;
          }
          if (t === -1)
            break;
          const r = i[t - 1] === "\r" ? t - 1 : t;
          n.enqueue(i.slice(0, r)), i = i.slice(t + 1);
        }
        Re(this, T, i);
      },
      flush: (i) => {
        if (V(this, T) === "")
          return;
        const n = e.allowCR && V(this, T).endsWith("\r") ? V(this, T).slice(0, -1) : V(this, T);
        i.enqueue(n);
      }
    }), Oe(this, T, "");
  }
}
T = /* @__PURE__ */ new WeakMap();
const {
  SvelteComponent: je,
  attr: w,
  binding_callbacks: Ge,
  create_component: Me,
  create_slot: He,
  destroy_component: Je,
  detach: X,
  element: he,
  get_all_dirty_from_scope: Ke,
  get_slot_changes: Qe,
  init: Ve,
  insert: Y,
  listen: fe,
  mount_component: Xe,
  run_all: Ye,
  safe_not_equal: Ze,
  set_data: Pe,
  space: be,
  src_url_equal: ae,
  text: pe,
  transition_in: ge,
  transition_out: we,
  update_slot_base: xe
} = window.__gradio__svelte__internal, { tick: $e, createEventDispatcher: ei } = window.__gradio__svelte__internal;
function ue(l) {
  let e, i, n;
  return {
    c() {
      e = he("img"), w(e, "class", "button-icon svelte-1gxyyj1"), ae(e.src, i = /*icon*/
      l[7].url) || w(e, "src", i), w(e, "alt", n = `${/*value*/
      l[1]} icon`);
    },
    m(t, f) {
      Y(t, e, f);
    },
    p(t, f) {
      f & /*icon*/
      128 && !ae(e.src, i = /*icon*/
      t[7].url) && w(e, "src", i), f & /*value*/
      2 && n !== (n = `${/*value*/
      t[1]} icon`) && w(e, "alt", n);
    },
    d(t) {
      t && X(e);
    }
  };
}
function ii(l) {
  let e;
  return {
    c() {
      e = pe(
        /*label*/
        l[0]
      );
    },
    m(i, n) {
      Y(i, e, n);
    },
    p(i, n) {
      n & /*label*/
      1 && Pe(
        e,
        /*label*/
        i[0]
      );
    },
    d(i) {
      i && X(e);
    }
  };
}
function li(l) {
  let e, i, n = (
    /*icon*/
    l[7] && ue(l)
  );
  const t = (
    /*#slots*/
    l[22].default
  ), f = He(
    t,
    l,
    /*$$scope*/
    l[24],
    null
  ), r = f || ii(l);
  return {
    c() {
      n && n.c(), e = be(), r && r.c();
    },
    m(u, a) {
      n && n.m(u, a), Y(u, e, a), r && r.m(u, a), i = !0;
    },
    p(u, a) {
      /*icon*/
      u[7] ? n ? n.p(u, a) : (n = ue(u), n.c(), n.m(e.parentNode, e)) : n && (n.d(1), n = null), f ? f.p && (!i || a & /*$$scope*/
      16777216) && xe(
        f,
        t,
        u,
        /*$$scope*/
        u[24],
        i ? Qe(
          t,
          /*$$scope*/
          u[24],
          a,
          null
        ) : Ke(
          /*$$scope*/
          u[24]
        ),
        null
      ) : r && r.p && (!i || a & /*label*/
      1) && r.p(u, i ? a : -1);
    },
    i(u) {
      i || (ge(r, u), i = !0);
    },
    o(u) {
      we(r, u), i = !1;
    },
    d(u) {
      u && X(e), n && n.d(u), r && r.d(u);
    }
  };
}
function ni(l) {
  let e, i, n, t, f, r, u, a, s, c;
  return u = new Ee({
    props: {
      size: (
        /*size*/
        l[6]
      ),
      variant: (
        /*variant*/
        l[10]
      ),
      elem_id: (
        /*elem_id*/
        l[2]
      ),
      elem_classes: (
        /*elem_classes*/
        l[3]
      ),
      visible: (
        /*visible*/
        l[4]
      ),
      scale: (
        /*scale*/
        l[8]
      ),
      min_width: (
        /*min_width*/
        l[9]
      ),
      disabled: (
        /*disabled*/
        l[11]
      ),
      $$slots: { default: [li] },
      $$scope: { ctx: l }
    }
  }), u.$on(
    "click",
    /*open_file_upload*/
    l[14]
  ), {
    c() {
      e = he("input"), r = be(), Me(u.$$.fragment), w(e, "class", "hide svelte-1gxyyj1"), w(
        e,
        "accept",
        /*accept_file_types*/
        l[13]
      ), w(e, "type", "file"), e.multiple = i = /*file_count*/
      l[5] === "multiple" || void 0, w(e, "webkitdirectory", n = /*file_count*/
      l[5] === "directory" || void 0), w(e, "mozdirectory", t = /*file_count*/
      l[5] === "directory" || void 0), w(e, "data-testid", f = /*label*/
      l[0] + "-upload-button");
    },
    m(o, h) {
      Y(o, e, h), l[23](e), Y(o, r, h), Xe(u, o, h), a = !0, s || (c = [
        fe(
          e,
          "change",
          /*load_files_from_upload*/
          l[15]
        ),
        fe(e, "click", ti)
      ], s = !0);
    },
    p(o, [h]) {
      (!a || h & /*accept_file_types*/
      8192) && w(
        e,
        "accept",
        /*accept_file_types*/
        o[13]
      ), (!a || h & /*file_count*/
      32 && i !== (i = /*file_count*/
      o[5] === "multiple" || void 0)) && (e.multiple = i), (!a || h & /*file_count*/
      32 && n !== (n = /*file_count*/
      o[5] === "directory" || void 0)) && w(e, "webkitdirectory", n), (!a || h & /*file_count*/
      32 && t !== (t = /*file_count*/
      o[5] === "directory" || void 0)) && w(e, "mozdirectory", t), (!a || h & /*label*/
      1 && f !== (f = /*label*/
      o[0] + "-upload-button")) && w(e, "data-testid", f);
      const g = {};
      h & /*size*/
      64 && (g.size = /*size*/
      o[6]), h & /*variant*/
      1024 && (g.variant = /*variant*/
      o[10]), h & /*elem_id*/
      4 && (g.elem_id = /*elem_id*/
      o[2]), h & /*elem_classes*/
      8 && (g.elem_classes = /*elem_classes*/
      o[3]), h & /*visible*/
      16 && (g.visible = /*visible*/
      o[4]), h & /*scale*/
      256 && (g.scale = /*scale*/
      o[8]), h & /*min_width*/
      512 && (g.min_width = /*min_width*/
      o[9]), h & /*disabled*/
      2048 && (g.disabled = /*disabled*/
      o[11]), h & /*$$scope, label, icon, value*/
      16777347 && (g.$$scope = { dirty: h, ctx: o }), u.$set(g);
    },
    i(o) {
      a || (ge(u.$$.fragment, o), a = !0);
    },
    o(o) {
      we(u.$$.fragment, o), a = !1;
    },
    d(o) {
      o && (X(e), X(r)), l[23](null), Je(u, o), s = !1, Ye(c);
    }
  };
}
function ti(l) {
  const e = l.target;
  e.value && (e.value = "");
}
function fi(l, e, i) {
  let { $$slots: n = {}, $$scope: t } = e;
  var f = this && this.__awaiter || function(_, v, q, z) {
    function F(y) {
      return y instanceof q ? y : new q(function(L) {
        L(y);
      });
    }
    return new (q || (q = Promise))(function(y, L) {
      function Q(N) {
        try {
          ie(z.next(N));
        } catch (le) {
          L(le);
        }
      }
      function ve(N) {
        try {
          ie(z.throw(N));
        } catch (le) {
          L(le);
        }
      }
      function ie(N) {
        N.done ? y(N.value) : F(N.value).then(Q, ve);
      }
      ie((z = z.apply(_, v || [])).next());
    });
  };
  let { elem_id: r = "" } = e, { elem_classes: u = [] } = e, { visible: a = !0 } = e, { interface_language: s } = e, { label: c } = e, { oldLabel: o } = e, { value: h } = e, { file_count: g } = e, { file_types: C = [] } = e, { root: S } = e, { size: D = "lg" } = e, { icon: m = null } = e, { scale: M = null } = e, { min_width: W = void 0 } = e, { variant: O = "secondary" } = e, { disabled: R = !1 } = e, { max_file_size: E = null } = e, { upload: H } = e;
  const B = ei();
  let A, J;
  C == null ? J = null : (C = C.map((_) => _.startsWith(".") ? _ : _ + "/*"), J = C.join(", "));
  function d() {
    B("click"), A.click();
  }
  function K(_) {
    return f(this, void 0, void 0, function* () {
      var v;
      let q = Array.from(_);
      if (!_.length)
        return;
      g === "single" && (q = [_[0]]);
      let z = yield Ae(q);
      yield $e();
      try {
        z = (v = yield H(z, S, void 0, E ?? 1 / 0)) === null || v === void 0 ? void 0 : v.filter((F) => F !== null);
      } catch (F) {
        B("error", F.message);
        return;
      }
      i(1, h = g === "single" ? z == null ? void 0 : z[0] : z), B("change", h), B("upload", h);
    });
  }
  function U(_) {
    return f(this, void 0, void 0, function* () {
      const v = _.target;
      v.files && (i(16, o = c), i(0, c = s.startsWith("fr") ? "Chargement ..." : "... Loading ..."), B("labelChange", c), yield K(v.files), i(0, c = o), B("labelChange", c));
    });
  }
  function j(_) {
    Ge[_ ? "unshift" : "push"](() => {
      A = _, i(12, A);
    });
  }
  return l.$$set = (_) => {
    "elem_id" in _ && i(2, r = _.elem_id), "elem_classes" in _ && i(3, u = _.elem_classes), "visible" in _ && i(4, a = _.visible), "interface_language" in _ && i(18, s = _.interface_language), "label" in _ && i(0, c = _.label), "oldLabel" in _ && i(16, o = _.oldLabel), "value" in _ && i(1, h = _.value), "file_count" in _ && i(5, g = _.file_count), "file_types" in _ && i(17, C = _.file_types), "root" in _ && i(19, S = _.root), "size" in _ && i(6, D = _.size), "icon" in _ && i(7, m = _.icon), "scale" in _ && i(8, M = _.scale), "min_width" in _ && i(9, W = _.min_width), "variant" in _ && i(10, O = _.variant), "disabled" in _ && i(11, R = _.disabled), "max_file_size" in _ && i(20, E = _.max_file_size), "upload" in _ && i(21, H = _.upload), "$$scope" in _ && i(24, t = _.$$scope);
  }, [
    c,
    h,
    r,
    u,
    a,
    g,
    D,
    m,
    M,
    W,
    O,
    R,
    A,
    J,
    d,
    U,
    o,
    C,
    s,
    S,
    E,
    H,
    n,
    j,
    t
  ];
}
class ai extends je {
  constructor(e) {
    super(), Ve(this, e, fi, ni, Ze, {
      elem_id: 2,
      elem_classes: 3,
      visible: 4,
      interface_language: 18,
      label: 0,
      oldLabel: 16,
      value: 1,
      file_count: 5,
      file_types: 17,
      root: 19,
      size: 6,
      icon: 7,
      scale: 8,
      min_width: 9,
      variant: 10,
      disabled: 11,
      max_file_size: 20,
      upload: 21
    });
  }
}
const {
  SvelteComponent: ui,
  create_component: _i,
  destroy_component: si,
  detach: oi,
  init: ci,
  insert: di,
  mount_component: ri,
  safe_not_equal: mi,
  set_data: hi,
  text: bi,
  transition_in: gi,
  transition_out: wi
} = window.__gradio__svelte__internal;
function vi(l) {
  let e = (
    /*label*/
    (l[0] ? (
      /*gradio*/
      l[14].i18n(
        /*label*/
        l[0]
      )
    ) : "") + ""
  ), i;
  return {
    c() {
      i = bi(e);
    },
    m(n, t) {
      di(n, i, t);
    },
    p(n, t) {
      t & /*label, gradio*/
      16385 && e !== (e = /*label*/
      (n[0] ? (
        /*gradio*/
        n[14].i18n(
          /*label*/
          n[0]
        )
      ) : "") + "") && hi(i, e);
    },
    d(n) {
      n && oi(i);
    }
  };
}
function ki(l) {
  let e, i;
  return e = new ai({
    props: {
      elem_id: (
        /*elem_id*/
        l[2]
      ),
      elem_classes: (
        /*elem_classes*/
        l[3]
      ),
      visible: (
        /*visible*/
        l[5]
      ),
      file_count: (
        /*file_count*/
        l[6]
      ),
      file_types: (
        /*file_types*/
        l[7]
      ),
      size: (
        /*size*/
        l[9]
      ),
      scale: (
        /*scale*/
        l[10]
      ),
      icon: (
        /*icon*/
        l[11]
      ),
      min_width: (
        /*min_width*/
        l[12]
      ),
      root: (
        /*root*/
        l[8]
      ),
      value: (
        /*value*/
        l[1]
      ),
      disabled: (
        /*disabled*/
        l[15]
      ),
      variant: (
        /*variant*/
        l[13]
      ),
      label: (
        /*label*/
        l[0]
      ),
      interface_language: (
        /*interface_language*/
        l[4]
      ),
      max_file_size: (
        /*gradio*/
        l[14].max_file_size
      ),
      upload: (
        /*gradio*/
        l[14].client.upload
      ),
      $$slots: { default: [vi] },
      $$scope: { ctx: l }
    }
  }), e.$on(
    "click",
    /*click_handler*/
    l[19]
  ), e.$on(
    "change",
    /*change_handler*/
    l[20]
  ), e.$on(
    "upload",
    /*upload_handler*/
    l[21]
  ), e.$on(
    "labelChange",
    /*handleLabelChange*/
    l[17]
  ), e.$on(
    "error",
    /*error_handler*/
    l[22]
  ), {
    c() {
      _i(e.$$.fragment);
    },
    m(n, t) {
      ri(e, n, t), i = !0;
    },
    p(n, [t]) {
      const f = {};
      t & /*elem_id*/
      4 && (f.elem_id = /*elem_id*/
      n[2]), t & /*elem_classes*/
      8 && (f.elem_classes = /*elem_classes*/
      n[3]), t & /*visible*/
      32 && (f.visible = /*visible*/
      n[5]), t & /*file_count*/
      64 && (f.file_count = /*file_count*/
      n[6]), t & /*file_types*/
      128 && (f.file_types = /*file_types*/
      n[7]), t & /*size*/
      512 && (f.size = /*size*/
      n[9]), t & /*scale*/
      1024 && (f.scale = /*scale*/
      n[10]), t & /*icon*/
      2048 && (f.icon = /*icon*/
      n[11]), t & /*min_width*/
      4096 && (f.min_width = /*min_width*/
      n[12]), t & /*root*/
      256 && (f.root = /*root*/
      n[8]), t & /*value*/
      2 && (f.value = /*value*/
      n[1]), t & /*disabled*/
      32768 && (f.disabled = /*disabled*/
      n[15]), t & /*variant*/
      8192 && (f.variant = /*variant*/
      n[13]), t & /*label*/
      1 && (f.label = /*label*/
      n[0]), t & /*interface_language*/
      16 && (f.interface_language = /*interface_language*/
      n[4]), t & /*gradio*/
      16384 && (f.max_file_size = /*gradio*/
      n[14].max_file_size), t & /*gradio*/
      16384 && (f.upload = /*gradio*/
      n[14].client.upload), t & /*$$scope, label, gradio*/
      16793601 && (f.$$scope = { dirty: t, ctx: n }), e.$set(f);
    },
    i(n) {
      i || (gi(e.$$.fragment, n), i = !0);
    },
    o(n) {
      wi(e.$$.fragment, n), i = !1;
    },
    d(n) {
      si(e, n);
    }
  };
}
function zi(l, e, i) {
  let n;
  var t = this && this.__awaiter || function(d, K, U, j) {
    function _(v) {
      return v instanceof U ? v : new U(function(q) {
        q(v);
      });
    }
    return new (U || (U = Promise))(function(v, q) {
      function z(L) {
        try {
          y(j.next(L));
        } catch (Q) {
          q(Q);
        }
      }
      function F(L) {
        try {
          y(j.throw(L));
        } catch (Q) {
          q(Q);
        }
      }
      function y(L) {
        L.done ? v(L.value) : _(L.value).then(z, F);
      }
      y((j = j.apply(d, K || [])).next());
    });
  };
  let { elem_id: f = "" } = e, { elem_classes: r = [] } = e, { interface_language: u = "fr" } = e, { visible: a = !0 } = e, { label: s } = e, { value: c } = e, { file_count: o } = e, { file_types: h = [] } = e, { root: g } = e, { size: C = "lg" } = e, { scale: S = null } = e, { icon: D = null } = e, { min_width: m = void 0 } = e, { variant: M = "secondary" } = e, { gradio: W } = e, { interactive: O } = e;
  function R(d, K) {
    return t(this, void 0, void 0, function* () {
      i(1, c = d), W.dispatch(K);
    });
  }
  function E(d) {
    i(0, s = d.detail);
  }
  const H = () => W.dispatch("click"), B = ({ detail: d }) => R(d, "change"), A = ({ detail: d }) => R(d, "upload"), J = ({ detail: d }) => {
    W.dispatch("error", d);
  };
  return l.$$set = (d) => {
    "elem_id" in d && i(2, f = d.elem_id), "elem_classes" in d && i(3, r = d.elem_classes), "interface_language" in d && i(4, u = d.interface_language), "visible" in d && i(5, a = d.visible), "label" in d && i(0, s = d.label), "value" in d && i(1, c = d.value), "file_count" in d && i(6, o = d.file_count), "file_types" in d && i(7, h = d.file_types), "root" in d && i(8, g = d.root), "size" in d && i(9, C = d.size), "scale" in d && i(10, S = d.scale), "icon" in d && i(11, D = d.icon), "min_width" in d && i(12, m = d.min_width), "variant" in d && i(13, M = d.variant), "gradio" in d && i(14, W = d.gradio), "interactive" in d && i(18, O = d.interactive);
  }, l.$$.update = () => {
    l.$$.dirty & /*interactive*/
    262144 && i(15, n = !O);
  }, [
    s,
    c,
    f,
    r,
    u,
    a,
    o,
    h,
    g,
    C,
    S,
    D,
    m,
    M,
    W,
    n,
    R,
    E,
    O,
    H,
    B,
    A,
    J
  ];
}
class qi extends ui {
  constructor(e) {
    super(), ci(this, e, zi, ki, mi, {
      elem_id: 2,
      elem_classes: 3,
      interface_language: 4,
      visible: 5,
      label: 0,
      value: 1,
      file_count: 6,
      file_types: 7,
      root: 8,
      size: 9,
      scale: 10,
      icon: 11,
      min_width: 12,
      variant: 13,
      gradio: 14,
      interactive: 18
    });
  }
}
export {
  ai as BaseUploadButton,
  qi as default
};
