const {
  SvelteComponent: Le,
  append: de,
  attr: g,
  bubble: qe,
  check_outros: ye,
  create_slot: re,
  detach: p,
  element: ne,
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
  toggle_class: G,
  transition_in: ee,
  transition_out: ie,
  update_slot_base: ge
} = window.__gradio__svelte__internal;
function Ee(l) {
  let e, i, t, n, f, r, c = (
    /*icon*/
    l[7] && se(l)
  );
  const a = (
    /*#slots*/
    l[12].default
  ), s = re(
    a,
    l,
    /*$$scope*/
    l[11],
    null
  );
  return {
    c() {
      e = ne("button"), c && c.c(), i = be(), s && s.c(), g(e, "class", t = /*size*/
      l[4] + " " + /*variant*/
      l[3] + " " + /*elem_classes*/
      l[1].join(" ") + " svelte-8huxfn"), g(
        e,
        "id",
        /*elem_id*/
        l[0]
      ), e.disabled = /*disabled*/
      l[8], G(e, "hidden", !/*visible*/
      l[2]), C(
        e,
        "flex-grow",
        /*scale*/
        l[9]
      ), C(
        e,
        "width",
        /*scale*/
        l[9] === 0 ? "fit-content" : null
      ), C(e, "min-width", typeof /*min_width*/
      l[10] == "number" ? `calc(min(${/*min_width*/
      l[10]}px, 100%))` : null);
    },
    m(u, o) {
      x(u, e, o), c && c.m(e, null), de(e, i), s && s.m(e, null), n = !0, f || (r = Be(
        e,
        "click",
        /*click_handler*/
        l[13]
      ), f = !0);
    },
    p(u, o) {
      /*icon*/
      u[7] ? c ? c.p(u, o) : (c = se(u), c.c(), c.m(e, i)) : c && (c.d(1), c = null), s && s.p && (!n || o & /*$$scope*/
      2048) && ge(
        s,
        a,
        u,
        /*$$scope*/
        u[11],
        n ? he(
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
      ), (!n || o & /*size, variant, elem_classes*/
      26 && t !== (t = /*size*/
      u[4] + " " + /*variant*/
      u[3] + " " + /*elem_classes*/
      u[1].join(" ") + " svelte-8huxfn")) && g(e, "class", t), (!n || o & /*elem_id*/
      1) && g(
        e,
        "id",
        /*elem_id*/
        u[0]
      ), (!n || o & /*disabled*/
      256) && (e.disabled = /*disabled*/
      u[8]), (!n || o & /*size, variant, elem_classes, visible*/
      30) && G(e, "hidden", !/*visible*/
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
      n || (ee(s, u), n = !0);
    },
    o(u) {
      ie(s, u), n = !1;
    },
    d(u) {
      u && p(e), c && c.d(), s && s.d(u), f = !1, r();
    }
  };
}
function Fe(l) {
  let e, i, t, n, f = (
    /*icon*/
    l[7] && oe(l)
  );
  const r = (
    /*#slots*/
    l[12].default
  ), c = re(
    r,
    l,
    /*$$scope*/
    l[11],
    null
  );
  return {
    c() {
      e = ne("a"), f && f.c(), i = be(), c && c.c(), g(
        e,
        "href",
        /*link*/
        l[6]
      ), g(e, "rel", "noopener noreferrer"), g(
        e,
        "aria-disabled",
        /*disabled*/
        l[8]
      ), g(e, "class", t = /*size*/
      l[4] + " " + /*variant*/
      l[3] + " " + /*elem_classes*/
      l[1].join(" ") + " svelte-8huxfn"), g(
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
      ), C(
        e,
        "flex-grow",
        /*scale*/
        l[9]
      ), C(
        e,
        "pointer-events",
        /*disabled*/
        l[8] ? "none" : null
      ), C(
        e,
        "width",
        /*scale*/
        l[9] === 0 ? "fit-content" : null
      ), C(e, "min-width", typeof /*min_width*/
      l[10] == "number" ? `calc(min(${/*min_width*/
      l[10]}px, 100%))` : null);
    },
    m(a, s) {
      x(a, e, s), f && f.m(e, null), de(e, i), c && c.m(e, null), n = !0;
    },
    p(a, s) {
      /*icon*/
      a[7] ? f ? f.p(a, s) : (f = oe(a), f.c(), f.m(e, i)) : f && (f.d(1), f = null), c && c.p && (!n || s & /*$$scope*/
      2048) && ge(
        c,
        r,
        a,
        /*$$scope*/
        a[11],
        n ? he(
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
      ), (!n || s & /*link*/
      64) && g(
        e,
        "href",
        /*link*/
        a[6]
      ), (!n || s & /*disabled*/
      256) && g(
        e,
        "aria-disabled",
        /*disabled*/
        a[8]
      ), (!n || s & /*size, variant, elem_classes*/
      26 && t !== (t = /*size*/
      a[4] + " " + /*variant*/
      a[3] + " " + /*elem_classes*/
      a[1].join(" ") + " svelte-8huxfn")) && g(e, "class", t), (!n || s & /*elem_id*/
      1) && g(
        e,
        "id",
        /*elem_id*/
        a[0]
      ), (!n || s & /*size, variant, elem_classes, visible*/
      30) && G(e, "hidden", !/*visible*/
      a[2]), (!n || s & /*size, variant, elem_classes, disabled*/
      282) && G(
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
      n || (ee(c, a), n = !0);
    },
    o(a) {
      ie(c, a), n = !1;
    },
    d(a) {
      a && p(e), f && f.d(), c && c.d(a);
    }
  };
}
function se(l) {
  let e, i, t;
  return {
    c() {
      e = ne("img"), g(e, "class", "button-icon svelte-8huxfn"), $(e.src, i = /*icon*/
      l[7].url) || g(e, "src", i), g(e, "alt", t = `${/*value*/
      l[5]} icon`);
    },
    m(n, f) {
      x(n, e, f);
    },
    p(n, f) {
      f & /*icon*/
      128 && !$(e.src, i = /*icon*/
      n[7].url) && g(e, "src", i), f & /*value*/
      32 && t !== (t = `${/*value*/
      n[5]} icon`) && g(e, "alt", t);
    },
    d(n) {
      n && p(e);
    }
  };
}
function oe(l) {
  let e, i, t;
  return {
    c() {
      e = ne("img"), g(e, "class", "button-icon svelte-8huxfn"), $(e.src, i = /*icon*/
      l[7].url) || g(e, "src", i), g(e, "alt", t = `${/*value*/
      l[5]} icon`);
    },
    m(n, f) {
      x(n, e, f);
    },
    p(n, f) {
      f & /*icon*/
      128 && !$(e.src, i = /*icon*/
      n[7].url) && g(e, "src", i), f & /*value*/
      32 && t !== (t = `${/*value*/
      n[5]} icon`) && g(e, "alt", t);
    },
    d(n) {
      n && p(e);
    }
  };
}
function Oe(l) {
  let e, i, t, n;
  const f = [Fe, Ee], r = [];
  function c(a, s) {
    return (
      /*link*/
      a[6] && /*link*/
      a[6].length > 0 ? 0 : 1
    );
  }
  return e = c(l), i = r[e] = f[e](l), {
    c() {
      i.c(), t = Se();
    },
    m(a, s) {
      r[e].m(a, s), x(a, t, s), n = !0;
    },
    p(a, [s]) {
      let u = e;
      e = c(a), e === u ? r[e].p(a, s) : (De(), ie(r[u], 1, 1, () => {
        r[u] = null;
      }), ye(), i = r[e], i ? i.p(a, s) : (i = r[e] = f[e](a), i.c()), ee(i, 1), i.m(t.parentNode, t));
    },
    i(a) {
      n || (ee(i), n = !0);
    },
    o(a) {
      ie(i), n = !1;
    },
    d(a) {
      a && p(t), r[e].d(a);
    }
  };
}
function Re(l, e, i) {
  let { $$slots: t = {}, $$scope: n } = e, { elem_id: f = "" } = e, { elem_classes: r = [] } = e, { visible: c = !0 } = e, { variant: a = "secondary" } = e, { size: s = "lg" } = e, { value: u = null } = e, { link: o = null } = e, { icon: m = null } = e, { disabled: b = !1 } = e, { scale: q = null } = e, { min_width: S = void 0 } = e;
  function y(h) {
    qe.call(this, l, h);
  }
  return l.$$set = (h) => {
    "elem_id" in h && i(0, f = h.elem_id), "elem_classes" in h && i(1, r = h.elem_classes), "visible" in h && i(2, c = h.visible), "variant" in h && i(3, a = h.variant), "size" in h && i(4, s = h.size), "value" in h && i(5, u = h.value), "link" in h && i(6, o = h.link), "icon" in h && i(7, m = h.icon), "disabled" in h && i(8, b = h.disabled), "scale" in h && i(9, q = h.scale), "min_width" in h && i(10, S = h.min_width), "$$scope" in h && i(11, n = h.$$scope);
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
    n,
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
var Ne = Object.defineProperty, Ue = (l, e, i) => e in l ? Ne(l, e, { enumerable: !0, configurable: !0, writable: !0, value: i }) : l[e] = i, T = (l, e, i) => (Ue(l, typeof e != "symbol" ? e + "" : e, i), i), ve = (l, e, i) => {
  if (!e.has(l))
    throw TypeError("Cannot " + i);
}, Z = (l, e, i) => (ve(l, e, "read from private field"), i ? i.call(l) : e.get(l)), Ge = (l, e, i) => {
  if (e.has(l))
    throw TypeError("Cannot add the same private member more than once");
  e instanceof WeakSet ? e.add(l) : e.set(l, i);
}, Me = (l, e, i, t) => (ve(l, e, "write to private field"), e.set(l, i), i), W;
new Intl.Collator(0, { numeric: 1 }).compare;
async function He(l, e) {
  return l.map(
    (i) => new Je({
      path: i.name,
      orig_name: i.name,
      blob: i,
      size: i.size,
      mime_type: i.type,
      is_stream: e
    })
  );
}
class Je {
  constructor({
    path: e,
    url: i,
    orig_name: t,
    size: n,
    blob: f,
    is_stream: r,
    mime_type: c,
    alt_text: a
  }) {
    T(this, "path"), T(this, "url"), T(this, "orig_name"), T(this, "size"), T(this, "blob"), T(this, "is_stream"), T(this, "mime_type"), T(this, "alt_text"), T(this, "meta", { _type: "gradio.FileData" }), this.path = e, this.url = i, this.orig_name = t, this.size = n, this.blob = i ? void 0 : f, this.is_stream = r, this.mime_type = c, this.alt_text = a;
  }
}
typeof process < "u" && process.versions && process.versions.node;
class Si extends TransformStream {
  /** Constructs a new instance. */
  constructor(e = { allowCR: !1 }) {
    super({
      transform: (i, t) => {
        for (i = Z(this, W) + i; ; ) {
          const n = i.indexOf(`
`), f = e.allowCR ? i.indexOf("\r") : -1;
          if (f !== -1 && f !== i.length - 1 && (n === -1 || n - 1 > f)) {
            t.enqueue(i.slice(0, f)), i = i.slice(f + 1);
            continue;
          }
          if (n === -1)
            break;
          const r = i[n - 1] === "\r" ? n - 1 : n;
          t.enqueue(i.slice(0, r)), i = i.slice(n + 1);
        }
        Me(this, W, i);
      },
      flush: (i) => {
        if (Z(this, W) === "")
          return;
        const t = e.allowCR && Z(this, W).endsWith("\r") ? Z(this, W).slice(0, -1) : Z(this, W);
        i.enqueue(t);
      }
    }), Ge(this, W, "");
  }
}
W = /* @__PURE__ */ new WeakMap();
const {
  SvelteComponent: Ke,
  append: Qe,
  attr: w,
  binding_callbacks: Ve,
  create_component: Xe,
  create_slot: Ye,
  destroy_component: Ze,
  detach: j,
  element: ue,
  get_all_dirty_from_scope: je,
  get_slot_changes: Pe,
  init: pe,
  insert: P,
  listen: le,
  mount_component: xe,
  run_all: we,
  safe_not_equal: $e,
  set_data: ei,
  space: ke,
  src_url_equal: _e,
  text: ii,
  transition_in: ze,
  transition_out: Ce,
  update_slot_base: li
} = window.__gradio__svelte__internal, { tick: ni, createEventDispatcher: ti } = window.__gradio__svelte__internal;
function ce(l) {
  let e, i, t;
  return {
    c() {
      e = ue("img"), w(e, "class", "button-icon svelte-oc0iyx"), _e(e.src, i = /*icon*/
      l[7].url) || w(e, "src", i), w(e, "alt", t = `${/*value*/
      l[1]} icon`);
    },
    m(n, f) {
      P(n, e, f);
    },
    p(n, f) {
      f & /*icon*/
      128 && !_e(e.src, i = /*icon*/
      n[7].url) && w(e, "src", i), f & /*value*/
      2 && t !== (t = `${/*value*/
      n[1]} icon`) && w(e, "alt", t);
    },
    d(n) {
      n && j(e);
    }
  };
}
function fi(l) {
  let e;
  return {
    c() {
      e = ii(
        /*label*/
        l[0]
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
      i && j(e);
    }
  };
}
function ai(l) {
  let e, i, t, n, f, r = (
    /*icon*/
    l[7] && ce(l)
  );
  const c = (
    /*#slots*/
    l[25].default
  ), a = Ye(
    c,
    l,
    /*$$scope*/
    l[27],
    null
  ), s = a || fi(l);
  return {
    c() {
      e = ue("div"), r && r.c(), i = ke(), s && s.c(), w(e, "role", "presentation"), w(e, "class", "dragdrop svelte-oc0iyx");
    },
    m(u, o) {
      P(u, e, o), r && r.m(e, null), Qe(e, i), s && s.m(e, null), t = !0, n || (f = [
        le(e, "dragover", si),
        le(
          e,
          "drop",
          /*drop_files*/
          l[16]
        )
      ], n = !0);
    },
    p(u, o) {
      /*icon*/
      u[7] ? r ? r.p(u, o) : (r = ce(u), r.c(), r.m(e, i)) : r && (r.d(1), r = null), a ? a.p && (!t || o & /*$$scope*/
      134217728) && li(
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
        ) : je(
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
      u && j(e), r && r.d(), s && s.d(u), n = !1, we(f);
    }
  };
}
function ui(l) {
  let e, i, t, n, f, r, c, a, s, u;
  return c = new Ae({
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
      $$slots: { default: [ai] },
      $$scope: { ctx: l }
    }
  }), c.$on(
    "click",
    /*open_file_upload*/
    l[14]
  ), {
    c() {
      e = ue("input"), r = ke(), Xe(c.$$.fragment), w(e, "class", "hide svelte-oc0iyx"), w(
        e,
        "accept",
        /*accept_file_types*/
        l[13]
      ), w(e, "type", "file"), e.multiple = i = /*file_count*/
      l[5] === "multiple" || void 0, w(e, "webkitdirectory", t = /*file_count*/
      l[5] === "directory" || void 0), w(e, "mozdirectory", n = /*file_count*/
      l[5] === "directory" || void 0), w(e, "data-testid", f = /*label*/
      l[0] + "-upload-button");
    },
    m(o, m) {
      P(o, e, m), l[26](e), P(o, r, m), xe(c, o, m), a = !0, s || (u = [
        le(
          e,
          "change",
          /*load_files_from_upload*/
          l[15]
        ),
        le(e, "click", oi)
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
      32 && n !== (n = /*file_count*/
      o[5] === "directory" || void 0)) && w(e, "mozdirectory", n), (!a || m & /*label*/
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
      o && (j(e), j(r)), l[26](null), Ze(c, o), s = !1, we(u);
    }
  };
}
function si(l) {
  l.preventDefault(), l.stopPropagation();
}
function oi(l) {
  const e = l.target;
  e.value && (e.value = "");
}
function _i(l, e, i) {
  let { $$slots: t = {}, $$scope: n } = e;
  var f = this && this.__awaiter || function(_, v, k, I) {
    function F(D) {
      return D instanceof k ? D : new k(function(L) {
        L(D);
      });
    }
    return new (k || (k = Promise))(function(D, L) {
      function Y(O) {
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
        O.done ? D(O.value) : F(O.value).then(Y, Ie);
      }
      fe((I = I.apply(_, v || [])).next());
    });
  };
  let { elem_id: r = "" } = e, { elem_classes: c = [] } = e, { visible: a = !0 } = e, { loading_message: s } = e, { label: u } = e, { oldLabel: o } = e, { interactive: m } = e, { oldInteractive: b } = e, { value: q } = e, { file_count: S } = e, { file_types: y = [] } = e, { root: h } = e, { size: M = "lg" } = e, { icon: H = null } = e, { scale: J = 1 } = e, { min_width: K = void 0 } = e, { variant: B = "secondary" } = e, { disabled: R = !1 } = e, { max_file_size: E = null } = e, { upload: Q } = e;
  const z = ti();
  let A, V;
  y == null ? V = null : (y = y.map((_) => _.startsWith(".") ? _ : _ + "/*"), V = y.join(", "));
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
      let I = yield He(k);
      yield ni();
      try {
        I = (v = yield Q(I, h, void 0, E ?? 1 / 0)) === null || v === void 0 ? void 0 : v.filter((F) => F !== null);
      } catch (F) {
        z("error", F.message);
        return;
      }
      i(1, q = S === "single" ? I == null ? void 0 : I[0] : I), z("change", q), z("upload", q);
    });
  }
  function X(_) {
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
    Ve[_ ? "unshift" : "push"](() => {
      A = _, i(12, A);
    });
  }
  return l.$$set = (_) => {
    "elem_id" in _ && i(2, r = _.elem_id), "elem_classes" in _ && i(3, c = _.elem_classes), "visible" in _ && i(4, a = _.visible), "loading_message" in _ && i(21, s = _.loading_message), "label" in _ && i(0, u = _.label), "oldLabel" in _ && i(17, o = _.oldLabel), "interactive" in _ && i(18, m = _.interactive), "oldInteractive" in _ && i(19, b = _.oldInteractive), "value" in _ && i(1, q = _.value), "file_count" in _ && i(5, S = _.file_count), "file_types" in _ && i(20, y = _.file_types), "root" in _ && i(22, h = _.root), "size" in _ && i(6, M = _.size), "icon" in _ && i(7, H = _.icon), "scale" in _ && i(8, J = _.scale), "min_width" in _ && i(9, K = _.min_width), "variant" in _ && i(10, B = _.variant), "disabled" in _ && i(11, R = _.disabled), "max_file_size" in _ && i(23, E = _.max_file_size), "upload" in _ && i(24, Q = _.upload), "$$scope" in _ && i(27, n = _.$$scope);
  }, [
    u,
    q,
    r,
    c,
    a,
    S,
    M,
    H,
    J,
    K,
    B,
    R,
    A,
    V,
    te,
    X,
    N,
    o,
    m,
    b,
    y,
    s,
    h,
    E,
    Q,
    t,
    U,
    n
  ];
}
class ci extends Ke {
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
function Li(l) {
  let e = (
    /*label*/
    (l[1] ? (
      /*gradio*/
      l[17].i18n(
        /*label*/
        l[1]
      )
    ) : "") + ""
  ), i;
  return {
    c() {
      i = zi(e);
    },
    m(t, n) {
      gi(t, i, n);
    },
    p(t, n) {
      n & /*label, gradio*/
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
function qi(l) {
  let e, i;
  return e = new ci({
    props: {
      elem_id: (
        /*elem_id*/
        l[3]
      ),
      elem_classes: (
        /*elem_classes*/
        l[4]
      ),
      visible: (
        /*visible*/
        l[6]
      ),
      file_count: (
        /*file_count*/
        l[9]
      ),
      file_types: (
        /*file_types*/
        l[10]
      ),
      size: (
        /*size*/
        l[12]
      ),
      scale: (
        /*scale*/
        l[13]
      ),
      icon: (
        /*icon*/
        l[14]
      ),
      min_width: (
        /*min_width*/
        l[15]
      ),
      root: (
        /*root*/
        l[11]
      ),
      value: (
        /*value*/
        l[2]
      ),
      disabled: (
        /*disabled*/
        l[18]
      ),
      variant: (
        /*variant*/
        l[16]
      ),
      label: (
        /*label*/
        l[1]
      ),
      oldLabel: (
        /*oldLabel*/
        l[7]
      ),
      interactive: (
        /*interactive*/
        l[0]
      ),
      oldInteractive: (
        /*oldInteractive*/
        l[8]
      ),
      loading_message: (
        /*loading_message*/
        l[5]
      ),
      max_file_size: (
        /*gradio*/
        l[17].max_file_size
      ),
      upload: (
        /*gradio*/
        l[17].client.upload
      ),
      $$slots: { default: [Li] },
      $$scope: { ctx: l }
    }
  }), e.$on(
    "click",
    /*click_handler*/
    l[22]
  ), e.$on(
    "change",
    /*change_handler*/
    l[23]
  ), e.$on(
    "upload",
    /*upload_handler*/
    l[24]
  ), e.$on(
    "labelChange",
    /*handle_label_change*/
    l[20]
  ), e.$on(
    "interactiveChange",
    /*handle_interactive_change*/
    l[21]
  ), e.$on(
    "error",
    /*error_handler*/
    l[25]
  ), {
    c() {
      ri(e.$$.fragment);
    },
    m(t, n) {
      vi(e, t, n), i = !0;
    },
    p(t, [n]) {
      const f = {};
      n & /*elem_id*/
      8 && (f.elem_id = /*elem_id*/
      t[3]), n & /*elem_classes*/
      16 && (f.elem_classes = /*elem_classes*/
      t[4]), n & /*visible*/
      64 && (f.visible = /*visible*/
      t[6]), n & /*file_count*/
      512 && (f.file_count = /*file_count*/
      t[9]), n & /*file_types*/
      1024 && (f.file_types = /*file_types*/
      t[10]), n & /*size*/
      4096 && (f.size = /*size*/
      t[12]), n & /*scale*/
      8192 && (f.scale = /*scale*/
      t[13]), n & /*icon*/
      16384 && (f.icon = /*icon*/
      t[14]), n & /*min_width*/
      32768 && (f.min_width = /*min_width*/
      t[15]), n & /*root*/
      2048 && (f.root = /*root*/
      t[11]), n & /*value*/
      4 && (f.value = /*value*/
      t[2]), n & /*disabled*/
      262144 && (f.disabled = /*disabled*/
      t[18]), n & /*variant*/
      65536 && (f.variant = /*variant*/
      t[16]), n & /*label*/
      2 && (f.label = /*label*/
      t[1]), n & /*oldLabel*/
      128 && (f.oldLabel = /*oldLabel*/
      t[7]), n & /*interactive*/
      1 && (f.interactive = /*interactive*/
      t[0]), n & /*oldInteractive*/
      256 && (f.oldInteractive = /*oldInteractive*/
      t[8]), n & /*loading_message*/
      32 && (f.loading_message = /*loading_message*/
      t[5]), n & /*gradio*/
      131072 && (f.max_file_size = /*gradio*/
      t[17].max_file_size), n & /*gradio*/
      131072 && (f.upload = /*gradio*/
      t[17].client.upload), n & /*$$scope, label, gradio*/
      134348802 && (f.$$scope = { dirty: n, ctx: t }), e.$set(f);
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
function yi(l, e, i) {
  let t;
  var n = this && this.__awaiter || function(d, X, N, U) {
    function _(v) {
      return v instanceof N ? v : new N(function(k) {
        k(v);
      });
    }
    return new (N || (N = Promise))(function(v, k) {
      function I(L) {
        try {
          D(U.next(L));
        } catch (Y) {
          k(Y);
        }
      }
      function F(L) {
        try {
          D(U.throw(L));
        } catch (Y) {
          k(Y);
        }
      }
      function D(L) {
        L.done ? v(L.value) : _(L.value).then(I, F);
      }
      D((U = U.apply(d, X || [])).next());
    });
  };
  let { elem_id: f = "" } = e, { elem_classes: r = [] } = e, { loading_message: c } = e, { visible: a = !0 } = e, { label: s } = e, { oldLabel: u } = e, { interactive: o } = e, { oldInteractive: m } = e, { value: b } = e, { file_count: q } = e, { file_types: S = [] } = e, { root: y } = e, { size: h = "lg" } = e, { scale: M = null } = e, { icon: H = null } = e, { min_width: J = void 0 } = e, { variant: K = "secondary" } = e, { gradio: B } = e;
  function R(d, X) {
    return n(this, void 0, void 0, function* () {
      i(2, b = d), B.dispatch(X);
    });
  }
  function E(d) {
    i(1, s = d.detail);
  }
  function Q(d) {
    i(0, o = d.detail);
  }
  const z = () => B.dispatch("click"), A = ({ detail: d }) => R(d, "change"), V = ({ detail: d }) => R(d, "upload"), te = ({ detail: d }) => {
    B.dispatch("error", d);
  };
  return l.$$set = (d) => {
    "elem_id" in d && i(3, f = d.elem_id), "elem_classes" in d && i(4, r = d.elem_classes), "loading_message" in d && i(5, c = d.loading_message), "visible" in d && i(6, a = d.visible), "label" in d && i(1, s = d.label), "oldLabel" in d && i(7, u = d.oldLabel), "interactive" in d && i(0, o = d.interactive), "oldInteractive" in d && i(8, m = d.oldInteractive), "value" in d && i(2, b = d.value), "file_count" in d && i(9, q = d.file_count), "file_types" in d && i(10, S = d.file_types), "root" in d && i(11, y = d.root), "size" in d && i(12, h = d.size), "scale" in d && i(13, M = d.scale), "icon" in d && i(14, H = d.icon), "min_width" in d && i(15, J = d.min_width), "variant" in d && i(16, K = d.variant), "gradio" in d && i(17, B = d.gradio);
  }, l.$$.update = () => {
    l.$$.dirty & /*interactive*/
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
    M,
    H,
    J,
    K,
    B,
    t,
    R,
    E,
    Q,
    z,
    A,
    V,
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
