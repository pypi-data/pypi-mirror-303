const {
  SvelteComponent: Le,
  append: de,
  attr: g,
  bubble: qe,
  check_outros: ye,
  create_slot: re,
  detach: p,
  element: le,
  empty: Se,
  get_all_dirty_from_scope: me,
  get_slot_changes: he,
  group_outros: De,
  init: Te,
  insert: x,
  listen: Be,
  safe_not_equal: We,
  set_style: C,
  space: be,
  src_url_equal: $,
  toggle_class: j,
  transition_in: ee,
  transition_out: ie,
  update_slot_base: ge
} = window.__gradio__svelte__internal;
function Ee(n) {
  let e, i, t, l, f, r, c = (
    /*icon*/
    n[7] && se(n)
  );
  const a = (
    /*#slots*/
    n[12].default
  ), s = re(
    a,
    n,
    /*$$scope*/
    n[11],
    null
  );
  return {
    c() {
      e = le("button"), c && c.c(), i = be(), s && s.c(), g(e, "class", t = /*size*/
      n[4] + " " + /*variant*/
      n[3] + " " + /*elem_classes*/
      n[1].join(" ") + " svelte-8huxfn"), g(
        e,
        "id",
        /*elem_id*/
        n[0]
      ), e.disabled = /*disabled*/
      n[8], j(e, "hidden", !/*visible*/
      n[2]), C(
        e,
        "flex-grow",
        /*scale*/
        n[9]
      ), C(
        e,
        "width",
        /*scale*/
        n[9] === 0 ? "fit-content" : null
      ), C(e, "min-width", typeof /*min_width*/
      n[10] == "number" ? `calc(min(${/*min_width*/
      n[10]}px, 100%))` : null);
    },
    m(u, o) {
      x(u, e, o), c && c.m(e, null), de(e, i), s && s.m(e, null), l = !0, f || (r = Be(
        e,
        "click",
        /*click_handler*/
        n[13]
      ), f = !0);
    },
    p(u, o) {
      /*icon*/
      u[7] ? c ? c.p(u, o) : (c = se(u), c.c(), c.m(e, i)) : c && (c.d(1), c = null), s && s.p && (!l || o & /*$$scope*/
      2048) && ge(
        s,
        a,
        u,
        /*$$scope*/
        u[11],
        l ? he(
          a,
          /*$$scope*/
          u[11],
          o,
          null
        ) : me(
          /*$$scope*/
          u[11]
        ),
        null
      ), (!l || o & /*size, variant, elem_classes*/
      26 && t !== (t = /*size*/
      u[4] + " " + /*variant*/
      u[3] + " " + /*elem_classes*/
      u[1].join(" ") + " svelte-8huxfn")) && g(e, "class", t), (!l || o & /*elem_id*/
      1) && g(
        e,
        "id",
        /*elem_id*/
        u[0]
      ), (!l || o & /*disabled*/
      256) && (e.disabled = /*disabled*/
      u[8]), (!l || o & /*size, variant, elem_classes, visible*/
      30) && j(e, "hidden", !/*visible*/
      u[2]), o & /*scale*/
      512 && C(
        e,
        "flex-grow",
        /*scale*/
        u[9]
      ), o & /*scale*/
      512 && C(
        e,
        "width",
        /*scale*/
        u[9] === 0 ? "fit-content" : null
      ), o & /*min_width*/
      1024 && C(e, "min-width", typeof /*min_width*/
      u[10] == "number" ? `calc(min(${/*min_width*/
      u[10]}px, 100%))` : null);
    },
    i(u) {
      l || (ee(s, u), l = !0);
    },
    o(u) {
      ie(s, u), l = !1;
    },
    d(u) {
      u && p(e), c && c.d(), s && s.d(u), f = !1, r();
    }
  };
}
function Fe(n) {
  let e, i, t, l, f = (
    /*icon*/
    n[7] && oe(n)
  );
  const r = (
    /*#slots*/
    n[12].default
  ), c = re(
    r,
    n,
    /*$$scope*/
    n[11],
    null
  );
  return {
    c() {
      e = le("a"), f && f.c(), i = be(), c && c.c(), g(
        e,
        "href",
        /*link*/
        n[6]
      ), g(e, "rel", "noopener noreferrer"), g(
        e,
        "aria-disabled",
        /*disabled*/
        n[8]
      ), g(e, "class", t = /*size*/
      n[4] + " " + /*variant*/
      n[3] + " " + /*elem_classes*/
      n[1].join(" ") + " svelte-8huxfn"), g(
        e,
        "id",
        /*elem_id*/
        n[0]
      ), j(e, "hidden", !/*visible*/
      n[2]), j(
        e,
        "disabled",
        /*disabled*/
        n[8]
      ), C(
        e,
        "flex-grow",
        /*scale*/
        n[9]
      ), C(
        e,
        "pointer-events",
        /*disabled*/
        n[8] ? "none" : null
      ), C(
        e,
        "width",
        /*scale*/
        n[9] === 0 ? "fit-content" : null
      ), C(e, "min-width", typeof /*min_width*/
      n[10] == "number" ? `calc(min(${/*min_width*/
      n[10]}px, 100%))` : null);
    },
    m(a, s) {
      x(a, e, s), f && f.m(e, null), de(e, i), c && c.m(e, null), l = !0;
    },
    p(a, s) {
      /*icon*/
      a[7] ? f ? f.p(a, s) : (f = oe(a), f.c(), f.m(e, i)) : f && (f.d(1), f = null), c && c.p && (!l || s & /*$$scope*/
      2048) && ge(
        c,
        r,
        a,
        /*$$scope*/
        a[11],
        l ? he(
          r,
          /*$$scope*/
          a[11],
          s,
          null
        ) : me(
          /*$$scope*/
          a[11]
        ),
        null
      ), (!l || s & /*link*/
      64) && g(
        e,
        "href",
        /*link*/
        a[6]
      ), (!l || s & /*disabled*/
      256) && g(
        e,
        "aria-disabled",
        /*disabled*/
        a[8]
      ), (!l || s & /*size, variant, elem_classes*/
      26 && t !== (t = /*size*/
      a[4] + " " + /*variant*/
      a[3] + " " + /*elem_classes*/
      a[1].join(" ") + " svelte-8huxfn")) && g(e, "class", t), (!l || s & /*elem_id*/
      1) && g(
        e,
        "id",
        /*elem_id*/
        a[0]
      ), (!l || s & /*size, variant, elem_classes, visible*/
      30) && j(e, "hidden", !/*visible*/
      a[2]), (!l || s & /*size, variant, elem_classes, disabled*/
      282) && j(
        e,
        "disabled",
        /*disabled*/
        a[8]
      ), s & /*scale*/
      512 && C(
        e,
        "flex-grow",
        /*scale*/
        a[9]
      ), s & /*disabled*/
      256 && C(
        e,
        "pointer-events",
        /*disabled*/
        a[8] ? "none" : null
      ), s & /*scale*/
      512 && C(
        e,
        "width",
        /*scale*/
        a[9] === 0 ? "fit-content" : null
      ), s & /*min_width*/
      1024 && C(e, "min-width", typeof /*min_width*/
      a[10] == "number" ? `calc(min(${/*min_width*/
      a[10]}px, 100%))` : null);
    },
    i(a) {
      l || (ee(c, a), l = !0);
    },
    o(a) {
      ie(c, a), l = !1;
    },
    d(a) {
      a && p(e), f && f.d(), c && c.d(a);
    }
  };
}
function se(n) {
  let e, i, t;
  return {
    c() {
      e = le("img"), g(e, "class", "button-icon svelte-8huxfn"), $(e.src, i = /*icon*/
      n[7].url) || g(e, "src", i), g(e, "alt", t = `${/*value*/
      n[5]} icon`);
    },
    m(l, f) {
      x(l, e, f);
    },
    p(l, f) {
      f & /*icon*/
      128 && !$(e.src, i = /*icon*/
      l[7].url) && g(e, "src", i), f & /*value*/
      32 && t !== (t = `${/*value*/
      l[5]} icon`) && g(e, "alt", t);
    },
    d(l) {
      l && p(e);
    }
  };
}
function oe(n) {
  let e, i, t;
  return {
    c() {
      e = le("img"), g(e, "class", "button-icon svelte-8huxfn"), $(e.src, i = /*icon*/
      n[7].url) || g(e, "src", i), g(e, "alt", t = `${/*value*/
      n[5]} icon`);
    },
    m(l, f) {
      x(l, e, f);
    },
    p(l, f) {
      f & /*icon*/
      128 && !$(e.src, i = /*icon*/
      l[7].url) && g(e, "src", i), f & /*value*/
      32 && t !== (t = `${/*value*/
      l[5]} icon`) && g(e, "alt", t);
    },
    d(l) {
      l && p(e);
    }
  };
}
function Oe(n) {
  let e, i, t, l;
  const f = [Fe, Ee], r = [];
  function c(a, s) {
    return (
      /*link*/
      a[6] && /*link*/
      a[6].length > 0 ? 0 : 1
    );
  }
  return e = c(n), i = r[e] = f[e](n), {
    c() {
      i.c(), t = Se();
    },
    m(a, s) {
      r[e].m(a, s), x(a, t, s), l = !0;
    },
    p(a, [s]) {
      let u = e;
      e = c(a), e === u ? r[e].p(a, s) : (De(), ie(r[u], 1, 1, () => {
        r[u] = null;
      }), ye(), i = r[e], i ? i.p(a, s) : (i = r[e] = f[e](a), i.c()), ee(i, 1), i.m(t.parentNode, t));
    },
    i(a) {
      l || (ee(i), l = !0);
    },
    o(a) {
      ie(i), l = !1;
    },
    d(a) {
      a && p(t), r[e].d(a);
    }
  };
}
function Re(n, e, i) {
  let { $$slots: t = {}, $$scope: l } = e, { elem_id: f = "" } = e, { elem_classes: r = [] } = e, { visible: c = !0 } = e, { variant: a = "secondary" } = e, { size: s = "lg" } = e, { value: u = null } = e, { link: o = null } = e, { icon: m = null } = e, { disabled: b = !1 } = e, { scale: q = null } = e, { min_width: S = void 0 } = e;
  function y(h) {
    qe.call(this, n, h);
  }
  return n.$$set = (h) => {
    "elem_id" in h && i(0, f = h.elem_id), "elem_classes" in h && i(1, r = h.elem_classes), "visible" in h && i(2, c = h.visible), "variant" in h && i(3, a = h.variant), "size" in h && i(4, s = h.size), "value" in h && i(5, u = h.value), "link" in h && i(6, o = h.link), "icon" in h && i(7, m = h.icon), "disabled" in h && i(8, b = h.disabled), "scale" in h && i(9, q = h.scale), "min_width" in h && i(10, S = h.min_width), "$$scope" in h && i(11, l = h.$$scope);
  }, [
    f,
    r,
    c,
    a,
    s,
    u,
    o,
    m,
    b,
    q,
    S,
    l,
    t,
    y
  ];
}
class Ae extends Le {
  constructor(e) {
    super(), Te(this, e, Re, Oe, We, {
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
var Ne = Object.defineProperty, Ue = (n, e, i) => e in n ? Ne(n, e, { enumerable: !0, configurable: !0, writable: !0, value: i }) : n[e] = i, T = (n, e, i) => (Ue(n, typeof e != "symbol" ? e + "" : e, i), i), ve = (n, e, i) => {
  if (!e.has(n))
    throw TypeError("Cannot " + i);
}, Y = (n, e, i) => (ve(n, e, "read from private field"), i ? i.call(n) : e.get(n)), je = (n, e, i) => {
  if (e.has(n))
    throw TypeError("Cannot add the same private member more than once");
  e instanceof WeakSet ? e.add(n) : e.set(n, i);
}, Ge = (n, e, i, t) => (ve(n, e, "write to private field"), e.set(n, i), i), W;
new Intl.Collator(0, { numeric: 1 }).compare;
async function Me(n, e) {
  return n.map(
    (i) => new He({
      path: i.name,
      orig_name: i.name,
      blob: i,
      size: i.size,
      mime_type: i.type,
      is_stream: e
    })
  );
}
class He {
  constructor({
    path: e,
    url: i,
    orig_name: t,
    size: l,
    blob: f,
    is_stream: r,
    mime_type: c,
    alt_text: a
  }) {
    T(this, "path"), T(this, "url"), T(this, "orig_name"), T(this, "size"), T(this, "blob"), T(this, "is_stream"), T(this, "mime_type"), T(this, "alt_text"), T(this, "meta", { _type: "gradio.FileData" }), this.path = e, this.url = i, this.orig_name = t, this.size = l, this.blob = i ? void 0 : f, this.is_stream = r, this.mime_type = c, this.alt_text = a;
  }
}
typeof process < "u" && process.versions && process.versions.node;
class Si extends TransformStream {
  /** Constructs a new instance. */
  constructor(e = { allowCR: !1 }) {
    super({
      transform: (i, t) => {
        for (i = Y(this, W) + i; ; ) {
          const l = i.indexOf(`
`), f = e.allowCR ? i.indexOf("\r") : -1;
          if (f !== -1 && f !== i.length - 1 && (l === -1 || l - 1 > f)) {
            t.enqueue(i.slice(0, f)), i = i.slice(f + 1);
            continue;
          }
          if (l === -1)
            break;
          const r = i[l - 1] === "\r" ? l - 1 : l;
          t.enqueue(i.slice(0, r)), i = i.slice(l + 1);
        }
        Ge(this, W, i);
      },
      flush: (i) => {
        if (Y(this, W) === "")
          return;
        const t = e.allowCR && Y(this, W).endsWith("\r") ? Y(this, W).slice(0, -1) : Y(this, W);
        i.enqueue(t);
      }
    }), je(this, W, "");
  }
}
W = /* @__PURE__ */ new WeakMap();
const {
  SvelteComponent: Je,
  append: Ke,
  attr: w,
  binding_callbacks: Qe,
  create_component: Ve,
  create_slot: Xe,
  destroy_component: Ye,
  detach: Z,
  element: ue,
  get_all_dirty_from_scope: Ze,
  get_slot_changes: Pe,
  init: pe,
  insert: P,
  listen: ne,
  mount_component: xe,
  run_all: we,
  safe_not_equal: $e,
  set_data: ei,
  space: ke,
  src_url_equal: _e,
  text: ii,
  transition_in: ze,
  transition_out: Ce,
  update_slot_base: ni
} = window.__gradio__svelte__internal, { tick: li, createEventDispatcher: ti } = window.__gradio__svelte__internal;
function ce(n) {
  let e, i, t;
  return {
    c() {
      e = ue("img"), w(e, "class", "button-icon svelte-1gxyyj1"), _e(e.src, i = /*icon*/
      n[7].url) || w(e, "src", i), w(e, "alt", t = `${/*value*/
      n[1]} icon`);
    },
    m(l, f) {
      P(l, e, f);
    },
    p(l, f) {
      f & /*icon*/
      128 && !_e(e.src, i = /*icon*/
      l[7].url) && w(e, "src", i), f & /*value*/
      2 && t !== (t = `${/*value*/
      l[1]} icon`) && w(e, "alt", t);
    },
    d(l) {
      l && Z(e);
    }
  };
}
function fi(n) {
  let e;
  return {
    c() {
      e = ii(
        /*label*/
        n[0]
      );
    },
    m(i, t) {
      P(i, e, t);
    },
    p(i, t) {
      t & /*label*/
      1 && ei(
        e,
        /*label*/
        i[0]
      );
    },
    d(i) {
      i && Z(e);
    }
  };
}
function ai(n) {
  let e, i, t, l, f, r = (
    /*icon*/
    n[7] && ce(n)
  );
  const c = (
    /*#slots*/
    n[25].default
  ), a = Xe(
    c,
    n,
    /*$$scope*/
    n[27],
    null
  ), s = a || fi(n);
  return {
    c() {
      e = ue("span"), r && r.c(), i = ke(), s && s.c(), w(e, "role", "presentation");
    },
    m(u, o) {
      P(u, e, o), r && r.m(e, null), Ke(e, i), s && s.m(e, null), t = !0, l || (f = [
        ne(e, "dragover", si),
        ne(
          e,
          "drop",
          /*drop_files*/
          n[16]
        )
      ], l = !0);
    },
    p(u, o) {
      /*icon*/
      u[7] ? r ? r.p(u, o) : (r = ce(u), r.c(), r.m(e, i)) : r && (r.d(1), r = null), a ? a.p && (!t || o & /*$$scope*/
      134217728) && ni(
        a,
        c,
        u,
        /*$$scope*/
        u[27],
        t ? Pe(
          c,
          /*$$scope*/
          u[27],
          o,
          null
        ) : Ze(
          /*$$scope*/
          u[27]
        ),
        null
      ) : s && s.p && (!t || o & /*label*/
      1) && s.p(u, t ? o : -1);
    },
    i(u) {
      t || (ze(s, u), t = !0);
    },
    o(u) {
      Ce(s, u), t = !1;
    },
    d(u) {
      u && Z(e), r && r.d(), s && s.d(u), l = !1, we(f);
    }
  };
}
function ui(n) {
  let e, i, t, l, f, r, c, a, s, u;
  return c = new Ae({
    props: {
      size: (
        /*size*/
        n[6]
      ),
      variant: (
        /*variant*/
        n[10]
      ),
      elem_id: (
        /*elem_id*/
        n[2]
      ),
      elem_classes: (
        /*elem_classes*/
        n[3]
      ),
      visible: (
        /*visible*/
        n[4]
      ),
      scale: (
        /*scale*/
        n[8]
      ),
      min_width: (
        /*min_width*/
        n[9]
      ),
      disabled: (
        /*disabled*/
        n[11]
      ),
      $$slots: { default: [ai] },
      $$scope: { ctx: n }
    }
  }), c.$on(
    "click",
    /*open_file_upload*/
    n[14]
  ), {
    c() {
      e = ue("input"), r = ke(), Ve(c.$$.fragment), w(e, "class", "hide svelte-1gxyyj1"), w(
        e,
        "accept",
        /*accept_file_types*/
        n[13]
      ), w(e, "type", "file"), e.multiple = i = /*file_count*/
      n[5] === "multiple" || void 0, w(e, "webkitdirectory", t = /*file_count*/
      n[5] === "directory" || void 0), w(e, "mozdirectory", l = /*file_count*/
      n[5] === "directory" || void 0), w(e, "data-testid", f = /*label*/
      n[0] + "-upload-button");
    },
    m(o, m) {
      P(o, e, m), n[26](e), P(o, r, m), xe(c, o, m), a = !0, s || (u = [
        ne(
          e,
          "change",
          /*load_files_from_upload*/
          n[15]
        ),
        ne(e, "click", oi)
      ], s = !0);
    },
    p(o, [m]) {
      (!a || m & /*accept_file_types*/
      8192) && w(
        e,
        "accept",
        /*accept_file_types*/
        o[13]
      ), (!a || m & /*file_count*/
      32 && i !== (i = /*file_count*/
      o[5] === "multiple" || void 0)) && (e.multiple = i), (!a || m & /*file_count*/
      32 && t !== (t = /*file_count*/
      o[5] === "directory" || void 0)) && w(e, "webkitdirectory", t), (!a || m & /*file_count*/
      32 && l !== (l = /*file_count*/
      o[5] === "directory" || void 0)) && w(e, "mozdirectory", l), (!a || m & /*label*/
      1 && f !== (f = /*label*/
      o[0] + "-upload-button")) && w(e, "data-testid", f);
      const b = {};
      m & /*size*/
      64 && (b.size = /*size*/
      o[6]), m & /*variant*/
      1024 && (b.variant = /*variant*/
      o[10]), m & /*elem_id*/
      4 && (b.elem_id = /*elem_id*/
      o[2]), m & /*elem_classes*/
      8 && (b.elem_classes = /*elem_classes*/
      o[3]), m & /*visible*/
      16 && (b.visible = /*visible*/
      o[4]), m & /*scale*/
      256 && (b.scale = /*scale*/
      o[8]), m & /*min_width*/
      512 && (b.min_width = /*min_width*/
      o[9]), m & /*disabled*/
      2048 && (b.disabled = /*disabled*/
      o[11]), m & /*$$scope, label, icon, value*/
      134217859 && (b.$$scope = { dirty: m, ctx: o }), c.$set(b);
    },
    i(o) {
      a || (ze(c.$$.fragment, o), a = !0);
    },
    o(o) {
      Ce(c.$$.fragment, o), a = !1;
    },
    d(o) {
      o && (Z(e), Z(r)), n[26](null), Ye(c, o), s = !1, we(u);
    }
  };
}
function si(n) {
  n.preventDefault(), n.stopPropagation();
}
function oi(n) {
  const e = n.target;
  e.value && (e.value = "");
}
function _i(n, e, i) {
  let { $$slots: t = {}, $$scope: l } = e;
  var f = this && this.__awaiter || function(_, v, k, I) {
    function F(D) {
      return D instanceof k ? D : new k(function(L) {
        L(D);
      });
    }
    return new (k || (k = Promise))(function(D, L) {
      function X(O) {
        try {
          fe(I.next(O));
        } catch (ae) {
          L(ae);
        }
      }
      function Ie(O) {
        try {
          fe(I.throw(O));
        } catch (ae) {
          L(ae);
        }
      }
      function fe(O) {
        O.done ? D(O.value) : F(O.value).then(X, Ie);
      }
      fe((I = I.apply(_, v || [])).next());
    });
  };
  let { elem_id: r = "" } = e, { elem_classes: c = [] } = e, { visible: a = !0 } = e, { loading_message: s } = e, { label: u } = e, { oldLabel: o } = e, { interactive: m } = e, { oldInteractive: b } = e, { value: q } = e, { file_count: S } = e, { file_types: y = [] } = e, { root: h } = e, { size: G = "lg" } = e, { icon: M = null } = e, { scale: H = 1 } = e, { min_width: J = void 0 } = e, { variant: B = "secondary" } = e, { disabled: R = !1 } = e, { max_file_size: E = null } = e, { upload: K } = e;
  const z = ti();
  let A, Q;
  y == null ? Q = null : (y = y.map((_) => _.startsWith(".") ? _ : _ + "/*"), Q = y.join(", "));
  function te() {
    z("click"), A.click();
  }
  function d(_) {
    return f(this, void 0, void 0, function* () {
      var v;
      let k = Array.from(_);
      if (!_.length)
        return;
      S === "single" && (k = [_[0]]);
      let I = yield Me(k);
      yield li();
      try {
        I = (v = yield K(I, h, void 0, E ?? 1 / 0)) === null || v === void 0 ? void 0 : v.filter((F) => F !== null);
      } catch (F) {
        z("error", F.message);
        return;
      }
      i(1, q = S === "single" ? I == null ? void 0 : I[0] : I), z("change", q), z("upload", q);
    });
  }
  function V(_) {
    return f(this, void 0, void 0, function* () {
      const v = _.target;
      v.files && (i(17, o = u), i(19, b = m), i(0, u = typeof s < "u" ? s : o), i(18, m = !(typeof s < "u")), z("labelChange", u), z("interactiveChange", m), yield d(v.files), i(0, u = o), i(18, m = b), z("labelChange", u), z("interactiveChange", m));
    });
  }
  function N(_) {
    return f(this, void 0, void 0, function* () {
      var v;
      console.log("drop"), _.preventDefault(), _.stopPropagation();
      const k = (v = _.dataTransfer) === null || v === void 0 ? void 0 : v.files;
      k && (i(17, o = u), i(19, b = m), i(0, u = typeof s < "u" ? s : o), i(18, m = !(typeof s < "u")), z("labelChange", u), z("interactiveChange", m), yield d(k), i(0, u = o), i(18, m = b), z("labelChange", u), z("interactiveChange", m));
    });
  }
  function U(_) {
    Qe[_ ? "unshift" : "push"](() => {
      A = _, i(12, A);
    });
  }
  return n.$$set = (_) => {
    "elem_id" in _ && i(2, r = _.elem_id), "elem_classes" in _ && i(3, c = _.elem_classes), "visible" in _ && i(4, a = _.visible), "loading_message" in _ && i(21, s = _.loading_message), "label" in _ && i(0, u = _.label), "oldLabel" in _ && i(17, o = _.oldLabel), "interactive" in _ && i(18, m = _.interactive), "oldInteractive" in _ && i(19, b = _.oldInteractive), "value" in _ && i(1, q = _.value), "file_count" in _ && i(5, S = _.file_count), "file_types" in _ && i(20, y = _.file_types), "root" in _ && i(22, h = _.root), "size" in _ && i(6, G = _.size), "icon" in _ && i(7, M = _.icon), "scale" in _ && i(8, H = _.scale), "min_width" in _ && i(9, J = _.min_width), "variant" in _ && i(10, B = _.variant), "disabled" in _ && i(11, R = _.disabled), "max_file_size" in _ && i(23, E = _.max_file_size), "upload" in _ && i(24, K = _.upload), "$$scope" in _ && i(27, l = _.$$scope);
  }, [
    u,
    q,
    r,
    c,
    a,
    S,
    G,
    M,
    H,
    J,
    B,
    R,
    A,
    Q,
    te,
    V,
    N,
    o,
    m,
    b,
    y,
    s,
    h,
    E,
    K,
    t,
    U,
    l
  ];
}
class ci extends Je {
  constructor(e) {
    super(), pe(this, e, _i, ui, $e, {
      elem_id: 2,
      elem_classes: 3,
      visible: 4,
      loading_message: 21,
      label: 0,
      oldLabel: 17,
      interactive: 18,
      oldInteractive: 19,
      value: 1,
      file_count: 5,
      file_types: 20,
      root: 22,
      size: 6,
      icon: 7,
      scale: 8,
      min_width: 9,
      variant: 10,
      disabled: 11,
      max_file_size: 23,
      upload: 24
    });
  }
}
const {
  SvelteComponent: di,
  create_component: ri,
  destroy_component: mi,
  detach: hi,
  init: bi,
  insert: gi,
  mount_component: vi,
  safe_not_equal: wi,
  set_data: ki,
  text: zi,
  transition_in: Ci,
  transition_out: Ii
} = window.__gradio__svelte__internal;
function Li(n) {
  let e = (
    /*label*/
    (n[1] ? (
      /*gradio*/
      n[17].i18n(
        /*label*/
        n[1]
      )
    ) : "") + ""
  ), i;
  return {
    c() {
      i = zi(e);
    },
    m(t, l) {
      gi(t, i, l);
    },
    p(t, l) {
      l & /*label, gradio*/
      131074 && e !== (e = /*label*/
      (t[1] ? (
        /*gradio*/
        t[17].i18n(
          /*label*/
          t[1]
        )
      ) : "") + "") && ki(i, e);
    },
    d(t) {
      t && hi(i);
    }
  };
}
function qi(n) {
  let e, i;
  return e = new ci({
    props: {
      elem_id: (
        /*elem_id*/
        n[3]
      ),
      elem_classes: (
        /*elem_classes*/
        n[4]
      ),
      visible: (
        /*visible*/
        n[6]
      ),
      file_count: (
        /*file_count*/
        n[9]
      ),
      file_types: (
        /*file_types*/
        n[10]
      ),
      size: (
        /*size*/
        n[12]
      ),
      scale: (
        /*scale*/
        n[13]
      ),
      icon: (
        /*icon*/
        n[14]
      ),
      min_width: (
        /*min_width*/
        n[15]
      ),
      root: (
        /*root*/
        n[11]
      ),
      value: (
        /*value*/
        n[2]
      ),
      disabled: (
        /*disabled*/
        n[18]
      ),
      variant: (
        /*variant*/
        n[16]
      ),
      label: (
        /*label*/
        n[1]
      ),
      oldLabel: (
        /*oldLabel*/
        n[7]
      ),
      interactive: (
        /*interactive*/
        n[0]
      ),
      oldInteractive: (
        /*oldInteractive*/
        n[8]
      ),
      loading_message: (
        /*loading_message*/
        n[5]
      ),
      max_file_size: (
        /*gradio*/
        n[17].max_file_size
      ),
      upload: (
        /*gradio*/
        n[17].client.upload
      ),
      $$slots: { default: [Li] },
      $$scope: { ctx: n }
    }
  }), e.$on(
    "click",
    /*click_handler*/
    n[22]
  ), e.$on(
    "change",
    /*change_handler*/
    n[23]
  ), e.$on(
    "upload",
    /*upload_handler*/
    n[24]
  ), e.$on(
    "labelChange",
    /*handle_label_change*/
    n[20]
  ), e.$on(
    "interactiveChange",
    /*handle_interactive_change*/
    n[21]
  ), e.$on(
    "error",
    /*error_handler*/
    n[25]
  ), {
    c() {
      ri(e.$$.fragment);
    },
    m(t, l) {
      vi(e, t, l), i = !0;
    },
    p(t, [l]) {
      const f = {};
      l & /*elem_id*/
      8 && (f.elem_id = /*elem_id*/
      t[3]), l & /*elem_classes*/
      16 && (f.elem_classes = /*elem_classes*/
      t[4]), l & /*visible*/
      64 && (f.visible = /*visible*/
      t[6]), l & /*file_count*/
      512 && (f.file_count = /*file_count*/
      t[9]), l & /*file_types*/
      1024 && (f.file_types = /*file_types*/
      t[10]), l & /*size*/
      4096 && (f.size = /*size*/
      t[12]), l & /*scale*/
      8192 && (f.scale = /*scale*/
      t[13]), l & /*icon*/
      16384 && (f.icon = /*icon*/
      t[14]), l & /*min_width*/
      32768 && (f.min_width = /*min_width*/
      t[15]), l & /*root*/
      2048 && (f.root = /*root*/
      t[11]), l & /*value*/
      4 && (f.value = /*value*/
      t[2]), l & /*disabled*/
      262144 && (f.disabled = /*disabled*/
      t[18]), l & /*variant*/
      65536 && (f.variant = /*variant*/
      t[16]), l & /*label*/
      2 && (f.label = /*label*/
      t[1]), l & /*oldLabel*/
      128 && (f.oldLabel = /*oldLabel*/
      t[7]), l & /*interactive*/
      1 && (f.interactive = /*interactive*/
      t[0]), l & /*oldInteractive*/
      256 && (f.oldInteractive = /*oldInteractive*/
      t[8]), l & /*loading_message*/
      32 && (f.loading_message = /*loading_message*/
      t[5]), l & /*gradio*/
      131072 && (f.max_file_size = /*gradio*/
      t[17].max_file_size), l & /*gradio*/
      131072 && (f.upload = /*gradio*/
      t[17].client.upload), l & /*$$scope, label, gradio*/
      134348802 && (f.$$scope = { dirty: l, ctx: t }), e.$set(f);
    },
    i(t) {
      i || (Ci(e.$$.fragment, t), i = !0);
    },
    o(t) {
      Ii(e.$$.fragment, t), i = !1;
    },
    d(t) {
      mi(e, t);
    }
  };
}
function yi(n, e, i) {
  let t;
  var l = this && this.__awaiter || function(d, V, N, U) {
    function _(v) {
      return v instanceof N ? v : new N(function(k) {
        k(v);
      });
    }
    return new (N || (N = Promise))(function(v, k) {
      function I(L) {
        try {
          D(U.next(L));
        } catch (X) {
          k(X);
        }
      }
      function F(L) {
        try {
          D(U.throw(L));
        } catch (X) {
          k(X);
        }
      }
      function D(L) {
        L.done ? v(L.value) : _(L.value).then(I, F);
      }
      D((U = U.apply(d, V || [])).next());
    });
  };
  let { elem_id: f = "" } = e, { elem_classes: r = [] } = e, { loading_message: c } = e, { visible: a = !0 } = e, { label: s } = e, { oldLabel: u } = e, { interactive: o } = e, { oldInteractive: m } = e, { value: b } = e, { file_count: q } = e, { file_types: S = [] } = e, { root: y } = e, { size: h = "lg" } = e, { scale: G = null } = e, { icon: M = null } = e, { min_width: H = void 0 } = e, { variant: J = "secondary" } = e, { gradio: B } = e;
  function R(d, V) {
    return l(this, void 0, void 0, function* () {
      i(2, b = d), B.dispatch(V);
    });
  }
  function E(d) {
    i(1, s = d.detail);
  }
  function K(d) {
    i(0, o = d.detail);
  }
  const z = () => B.dispatch("click"), A = ({ detail: d }) => R(d, "change"), Q = ({ detail: d }) => R(d, "upload"), te = ({ detail: d }) => {
    B.dispatch("error", d);
  };
  return n.$$set = (d) => {
    "elem_id" in d && i(3, f = d.elem_id), "elem_classes" in d && i(4, r = d.elem_classes), "loading_message" in d && i(5, c = d.loading_message), "visible" in d && i(6, a = d.visible), "label" in d && i(1, s = d.label), "oldLabel" in d && i(7, u = d.oldLabel), "interactive" in d && i(0, o = d.interactive), "oldInteractive" in d && i(8, m = d.oldInteractive), "value" in d && i(2, b = d.value), "file_count" in d && i(9, q = d.file_count), "file_types" in d && i(10, S = d.file_types), "root" in d && i(11, y = d.root), "size" in d && i(12, h = d.size), "scale" in d && i(13, G = d.scale), "icon" in d && i(14, M = d.icon), "min_width" in d && i(15, H = d.min_width), "variant" in d && i(16, J = d.variant), "gradio" in d && i(17, B = d.gradio);
  }, n.$$.update = () => {
    n.$$.dirty & /*interactive*/
    1 && i(18, t = !o);
  }, [
    o,
    s,
    b,
    f,
    r,
    c,
    a,
    u,
    m,
    q,
    S,
    y,
    h,
    G,
    M,
    H,
    J,
    B,
    t,
    R,
    E,
    K,
    z,
    A,
    Q,
    te
  ];
}
class Di extends di {
  constructor(e) {
    super(), bi(this, e, yi, qi, wi, {
      elem_id: 3,
      elem_classes: 4,
      loading_message: 5,
      visible: 6,
      label: 1,
      oldLabel: 7,
      interactive: 0,
      oldInteractive: 8,
      value: 2,
      file_count: 9,
      file_types: 10,
      root: 11,
      size: 12,
      scale: 13,
      icon: 14,
      min_width: 15,
      variant: 16,
      gradio: 17
    });
  }
}
export {
  ci as BaseUploadButton,
  Di as default
};
