const {
  SvelteComponent: Ce,
  append: _e,
  attr: b,
  bubble: Le,
  check_outros: qe,
  create_slot: ce,
  detach: Z,
  element: le,
  empty: ye,
  get_all_dirty_from_scope: de,
  get_slot_changes: re,
  group_outros: Se,
  init: Ie,
  insert: P,
  listen: De,
  safe_not_equal: Te,
  set_style: C,
  space: me,
  src_url_equal: p,
  toggle_class: H,
  transition_in: x,
  transition_out: $,
  update_slot_base: he
} = window.__gradio__svelte__internal;
function Be(i) {
  let e, l, t, n, f, r, c = (
    /*icon*/
    i[7] && ae(i)
  );
  const a = (
    /*#slots*/
    i[12].default
  ), u = ce(
    a,
    i,
    /*$$scope*/
    i[11],
    null
  );
  return {
    c() {
      e = le("button"), c && c.c(), l = me(), u && u.c(), b(e, "class", t = /*size*/
      i[4] + " " + /*variant*/
      i[3] + " " + /*elem_classes*/
      i[1].join(" ") + " svelte-8huxfn"), b(
        e,
        "id",
        /*elem_id*/
        i[0]
      ), e.disabled = /*disabled*/
      i[8], H(e, "hidden", !/*visible*/
      i[2]), C(
        e,
        "flex-grow",
        /*scale*/
        i[9]
      ), C(
        e,
        "width",
        /*scale*/
        i[9] === 0 ? "fit-content" : null
      ), C(e, "min-width", typeof /*min_width*/
      i[10] == "number" ? `calc(min(${/*min_width*/
      i[10]}px, 100%))` : null);
    },
    m(s, o) {
      P(s, e, o), c && c.m(e, null), _e(e, l), u && u.m(e, null), n = !0, f || (r = De(
        e,
        "click",
        /*click_handler*/
        i[13]
      ), f = !0);
    },
    p(s, o) {
      /*icon*/
      s[7] ? c ? c.p(s, o) : (c = ae(s), c.c(), c.m(e, l)) : c && (c.d(1), c = null), u && u.p && (!n || o & /*$$scope*/
      2048) && he(
        u,
        a,
        s,
        /*$$scope*/
        s[11],
        n ? re(
          a,
          /*$$scope*/
          s[11],
          o,
          null
        ) : de(
          /*$$scope*/
          s[11]
        ),
        null
      ), (!n || o & /*size, variant, elem_classes*/
      26 && t !== (t = /*size*/
      s[4] + " " + /*variant*/
      s[3] + " " + /*elem_classes*/
      s[1].join(" ") + " svelte-8huxfn")) && b(e, "class", t), (!n || o & /*elem_id*/
      1) && b(
        e,
        "id",
        /*elem_id*/
        s[0]
      ), (!n || o & /*disabled*/
      256) && (e.disabled = /*disabled*/
      s[8]), (!n || o & /*size, variant, elem_classes, visible*/
      30) && H(e, "hidden", !/*visible*/
      s[2]), o & /*scale*/
      512 && C(
        e,
        "flex-grow",
        /*scale*/
        s[9]
      ), o & /*scale*/
      512 && C(
        e,
        "width",
        /*scale*/
        s[9] === 0 ? "fit-content" : null
      ), o & /*min_width*/
      1024 && C(e, "min-width", typeof /*min_width*/
      s[10] == "number" ? `calc(min(${/*min_width*/
      s[10]}px, 100%))` : null);
    },
    i(s) {
      n || (x(u, s), n = !0);
    },
    o(s) {
      $(u, s), n = !1;
    },
    d(s) {
      s && Z(e), c && c.d(), u && u.d(s), f = !1, r();
    }
  };
}
function We(i) {
  let e, l, t, n, f = (
    /*icon*/
    i[7] && se(i)
  );
  const r = (
    /*#slots*/
    i[12].default
  ), c = ce(
    r,
    i,
    /*$$scope*/
    i[11],
    null
  );
  return {
    c() {
      e = le("a"), f && f.c(), l = me(), c && c.c(), b(
        e,
        "href",
        /*link*/
        i[6]
      ), b(e, "rel", "noopener noreferrer"), b(
        e,
        "aria-disabled",
        /*disabled*/
        i[8]
      ), b(e, "class", t = /*size*/
      i[4] + " " + /*variant*/
      i[3] + " " + /*elem_classes*/
      i[1].join(" ") + " svelte-8huxfn"), b(
        e,
        "id",
        /*elem_id*/
        i[0]
      ), H(e, "hidden", !/*visible*/
      i[2]), H(
        e,
        "disabled",
        /*disabled*/
        i[8]
      ), C(
        e,
        "flex-grow",
        /*scale*/
        i[9]
      ), C(
        e,
        "pointer-events",
        /*disabled*/
        i[8] ? "none" : null
      ), C(
        e,
        "width",
        /*scale*/
        i[9] === 0 ? "fit-content" : null
      ), C(e, "min-width", typeof /*min_width*/
      i[10] == "number" ? `calc(min(${/*min_width*/
      i[10]}px, 100%))` : null);
    },
    m(a, u) {
      P(a, e, u), f && f.m(e, null), _e(e, l), c && c.m(e, null), n = !0;
    },
    p(a, u) {
      /*icon*/
      a[7] ? f ? f.p(a, u) : (f = se(a), f.c(), f.m(e, l)) : f && (f.d(1), f = null), c && c.p && (!n || u & /*$$scope*/
      2048) && he(
        c,
        r,
        a,
        /*$$scope*/
        a[11],
        n ? re(
          r,
          /*$$scope*/
          a[11],
          u,
          null
        ) : de(
          /*$$scope*/
          a[11]
        ),
        null
      ), (!n || u & /*link*/
      64) && b(
        e,
        "href",
        /*link*/
        a[6]
      ), (!n || u & /*disabled*/
      256) && b(
        e,
        "aria-disabled",
        /*disabled*/
        a[8]
      ), (!n || u & /*size, variant, elem_classes*/
      26 && t !== (t = /*size*/
      a[4] + " " + /*variant*/
      a[3] + " " + /*elem_classes*/
      a[1].join(" ") + " svelte-8huxfn")) && b(e, "class", t), (!n || u & /*elem_id*/
      1) && b(
        e,
        "id",
        /*elem_id*/
        a[0]
      ), (!n || u & /*size, variant, elem_classes, visible*/
      30) && H(e, "hidden", !/*visible*/
      a[2]), (!n || u & /*size, variant, elem_classes, disabled*/
      282) && H(
        e,
        "disabled",
        /*disabled*/
        a[8]
      ), u & /*scale*/
      512 && C(
        e,
        "flex-grow",
        /*scale*/
        a[9]
      ), u & /*disabled*/
      256 && C(
        e,
        "pointer-events",
        /*disabled*/
        a[8] ? "none" : null
      ), u & /*scale*/
      512 && C(
        e,
        "width",
        /*scale*/
        a[9] === 0 ? "fit-content" : null
      ), u & /*min_width*/
      1024 && C(e, "min-width", typeof /*min_width*/
      a[10] == "number" ? `calc(min(${/*min_width*/
      a[10]}px, 100%))` : null);
    },
    i(a) {
      n || (x(c, a), n = !0);
    },
    o(a) {
      $(c, a), n = !1;
    },
    d(a) {
      a && Z(e), f && f.d(), c && c.d(a);
    }
  };
}
function ae(i) {
  let e, l, t;
  return {
    c() {
      e = le("img"), b(e, "class", "button-icon svelte-8huxfn"), p(e.src, l = /*icon*/
      i[7].url) || b(e, "src", l), b(e, "alt", t = `${/*value*/
      i[5]} icon`);
    },
    m(n, f) {
      P(n, e, f);
    },
    p(n, f) {
      f & /*icon*/
      128 && !p(e.src, l = /*icon*/
      n[7].url) && b(e, "src", l), f & /*value*/
      32 && t !== (t = `${/*value*/
      n[5]} icon`) && b(e, "alt", t);
    },
    d(n) {
      n && Z(e);
    }
  };
}
function se(i) {
  let e, l, t;
  return {
    c() {
      e = le("img"), b(e, "class", "button-icon svelte-8huxfn"), p(e.src, l = /*icon*/
      i[7].url) || b(e, "src", l), b(e, "alt", t = `${/*value*/
      i[5]} icon`);
    },
    m(n, f) {
      P(n, e, f);
    },
    p(n, f) {
      f & /*icon*/
      128 && !p(e.src, l = /*icon*/
      n[7].url) && b(e, "src", l), f & /*value*/
      32 && t !== (t = `${/*value*/
      n[5]} icon`) && b(e, "alt", t);
    },
    d(n) {
      n && Z(e);
    }
  };
}
function Ee(i) {
  let e, l, t, n;
  const f = [We, Be], r = [];
  function c(a, u) {
    return (
      /*link*/
      a[6] && /*link*/
      a[6].length > 0 ? 0 : 1
    );
  }
  return e = c(i), l = r[e] = f[e](i), {
    c() {
      l.c(), t = ye();
    },
    m(a, u) {
      r[e].m(a, u), P(a, t, u), n = !0;
    },
    p(a, [u]) {
      let s = e;
      e = c(a), e === s ? r[e].p(a, u) : (Se(), $(r[s], 1, 1, () => {
        r[s] = null;
      }), qe(), l = r[e], l ? l.p(a, u) : (l = r[e] = f[e](a), l.c()), x(l, 1), l.m(t.parentNode, t));
    },
    i(a) {
      n || (x(l), n = !0);
    },
    o(a) {
      $(l), n = !1;
    },
    d(a) {
      a && Z(t), r[e].d(a);
    }
  };
}
function Fe(i, e, l) {
  let { $$slots: t = {}, $$scope: n } = e, { elem_id: f = "" } = e, { elem_classes: r = [] } = e, { visible: c = !0 } = e, { variant: a = "secondary" } = e, { size: u = "lg" } = e, { value: s = null } = e, { link: o = null } = e, { icon: h = null } = e, { disabled: g = !1 } = e, { scale: L = null } = e, { min_width: S = void 0 } = e;
  function B(m) {
    Le.call(this, i, m);
  }
  return i.$$set = (m) => {
    "elem_id" in m && l(0, f = m.elem_id), "elem_classes" in m && l(1, r = m.elem_classes), "visible" in m && l(2, c = m.visible), "variant" in m && l(3, a = m.variant), "size" in m && l(4, u = m.size), "value" in m && l(5, s = m.value), "link" in m && l(6, o = m.link), "icon" in m && l(7, h = m.icon), "disabled" in m && l(8, g = m.disabled), "scale" in m && l(9, L = m.scale), "min_width" in m && l(10, S = m.min_width), "$$scope" in m && l(11, n = m.$$scope);
  }, [
    f,
    r,
    c,
    a,
    u,
    s,
    o,
    h,
    g,
    L,
    S,
    n,
    t,
    B
  ];
}
class Oe extends Ce {
  constructor(e) {
    super(), Ie(this, e, Fe, Ee, Te, {
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
var Re = Object.defineProperty, Ae = (i, e, l) => e in i ? Re(i, e, { enumerable: !0, configurable: !0, writable: !0, value: l }) : i[e] = l, T = (i, e, l) => (Ae(i, typeof e != "symbol" ? e + "" : e, l), l), be = (i, e, l) => {
  if (!e.has(i))
    throw TypeError("Cannot " + l);
}, V = (i, e, l) => (be(i, e, "read from private field"), l ? l.call(i) : e.get(i)), Ne = (i, e, l) => {
  if (e.has(i))
    throw TypeError("Cannot add the same private member more than once");
  e instanceof WeakSet ? e.add(i) : e.set(i, l);
}, Ue = (i, e, l, t) => (be(i, e, "write to private field"), e.set(i, l), l), E;
new Intl.Collator(0, { numeric: 1 }).compare;
async function je(i, e) {
  return i.map(
    (l) => new Ge({
      path: l.name,
      orig_name: l.name,
      blob: l,
      size: l.size,
      mime_type: l.type,
      is_stream: e
    })
  );
}
class Ge {
  constructor({
    path: e,
    url: l,
    orig_name: t,
    size: n,
    blob: f,
    is_stream: r,
    mime_type: c,
    alt_text: a
  }) {
    T(this, "path"), T(this, "url"), T(this, "orig_name"), T(this, "size"), T(this, "blob"), T(this, "is_stream"), T(this, "mime_type"), T(this, "alt_text"), T(this, "meta", { _type: "gradio.FileData" }), this.path = e, this.url = l, this.orig_name = t, this.size = n, this.blob = l ? void 0 : f, this.is_stream = r, this.mime_type = c, this.alt_text = a;
  }
}
typeof process < "u" && process.versions && process.versions.node;
class yl extends TransformStream {
  /** Constructs a new instance. */
  constructor(e = { allowCR: !1 }) {
    super({
      transform: (l, t) => {
        for (l = V(this, E) + l; ; ) {
          const n = l.indexOf(`
`), f = e.allowCR ? l.indexOf("\r") : -1;
          if (f !== -1 && f !== l.length - 1 && (n === -1 || n - 1 > f)) {
            t.enqueue(l.slice(0, f)), l = l.slice(f + 1);
            continue;
          }
          if (n === -1)
            break;
          const r = l[n - 1] === "\r" ? n - 1 : n;
          t.enqueue(l.slice(0, r)), l = l.slice(n + 1);
        }
        Ue(this, E, l);
      },
      flush: (l) => {
        if (V(this, E) === "")
          return;
        const t = e.allowCR && V(this, E).endsWith("\r") ? V(this, E).slice(0, -1) : V(this, E);
        l.enqueue(t);
      }
    }), Ne(this, E, "");
  }
}
E = /* @__PURE__ */ new WeakMap();
const {
  SvelteComponent: Me,
  append: He,
  attr: k,
  binding_callbacks: Je,
  create_component: Ke,
  create_slot: Qe,
  destroy_component: Ve,
  detach: X,
  element: fe,
  get_all_dirty_from_scope: Xe,
  get_slot_changes: Ye,
  init: Ze,
  insert: Y,
  listen: ee,
  mount_component: Pe,
  run_all: ge,
  safe_not_equal: pe,
  set_data: xe,
  space: ve,
  src_url_equal: ue,
  text: $e,
  transition_in: we,
  transition_out: ke,
  update_slot_base: el
} = window.__gradio__svelte__internal, { tick: ll, createEventDispatcher: il } = window.__gradio__svelte__internal;
function oe(i) {
  let e, l, t;
  return {
    c() {
      e = fe("img"), k(e, "class", "button-icon svelte-1gxyyj1"), ue(e.src, l = /*icon*/
      i[7].url) || k(e, "src", l), k(e, "alt", t = `${/*value*/
      i[1]} icon`);
    },
    m(n, f) {
      Y(n, e, f);
    },
    p(n, f) {
      f & /*icon*/
      128 && !ue(e.src, l = /*icon*/
      n[7].url) && k(e, "src", l), f & /*value*/
      2 && t !== (t = `${/*value*/
      n[1]} icon`) && k(e, "alt", t);
    },
    d(n) {
      n && X(e);
    }
  };
}
function nl(i) {
  let e;
  return {
    c() {
      e = $e(
        /*label*/
        i[0]
      );
    },
    m(l, t) {
      Y(l, e, t);
    },
    p(l, t) {
      t & /*label*/
      1 && xe(
        e,
        /*label*/
        l[0]
      );
    },
    d(l) {
      l && X(e);
    }
  };
}
function tl(i) {
  let e, l, t, n, f, r = (
    /*icon*/
    i[7] && oe(i)
  );
  const c = (
    /*#slots*/
    i[23].default
  ), a = Qe(
    c,
    i,
    /*$$scope*/
    i[25],
    null
  ), u = a || nl(i);
  return {
    c() {
      e = fe("span"), r && r.c(), l = ve(), u && u.c(), k(e, "role", "presentation");
    },
    m(s, o) {
      Y(s, e, o), r && r.m(e, null), He(e, l), u && u.m(e, null), t = !0, n || (f = [
        ee(e, "dragover", al),
        ee(
          e,
          "drop",
          /*drop_files*/
          i[16]
        )
      ], n = !0);
    },
    p(s, o) {
      /*icon*/
      s[7] ? r ? r.p(s, o) : (r = oe(s), r.c(), r.m(e, l)) : r && (r.d(1), r = null), a ? a.p && (!t || o & /*$$scope*/
      33554432) && el(
        a,
        c,
        s,
        /*$$scope*/
        s[25],
        t ? Ye(
          c,
          /*$$scope*/
          s[25],
          o,
          null
        ) : Xe(
          /*$$scope*/
          s[25]
        ),
        null
      ) : u && u.p && (!t || o & /*label*/
      1) && u.p(s, t ? o : -1);
    },
    i(s) {
      t || (we(u, s), t = !0);
    },
    o(s) {
      ke(u, s), t = !1;
    },
    d(s) {
      s && X(e), r && r.d(), u && u.d(s), n = !1, ge(f);
    }
  };
}
function fl(i) {
  let e, l, t, n, f, r, c, a, u, s;
  return c = new Oe({
    props: {
      size: (
        /*size*/
        i[6]
      ),
      variant: (
        /*variant*/
        i[10]
      ),
      elem_id: (
        /*elem_id*/
        i[2]
      ),
      elem_classes: (
        /*elem_classes*/
        i[3]
      ),
      visible: (
        /*visible*/
        i[4]
      ),
      scale: (
        /*scale*/
        i[8]
      ),
      min_width: (
        /*min_width*/
        i[9]
      ),
      disabled: (
        /*disabled*/
        i[11]
      ),
      $$slots: { default: [tl] },
      $$scope: { ctx: i }
    }
  }), c.$on(
    "click",
    /*open_file_upload*/
    i[14]
  ), {
    c() {
      e = fe("input"), r = ve(), Ke(c.$$.fragment), k(e, "class", "hide svelte-1gxyyj1"), k(
        e,
        "accept",
        /*accept_file_types*/
        i[13]
      ), k(e, "type", "file"), e.multiple = l = /*file_count*/
      i[5] === "multiple" || void 0, k(e, "webkitdirectory", t = /*file_count*/
      i[5] === "directory" || void 0), k(e, "mozdirectory", n = /*file_count*/
      i[5] === "directory" || void 0), k(e, "data-testid", f = /*label*/
      i[0] + "-upload-button");
    },
    m(o, h) {
      Y(o, e, h), i[24](e), Y(o, r, h), Pe(c, o, h), a = !0, u || (s = [
        ee(
          e,
          "change",
          /*load_files_from_upload*/
          i[15]
        ),
        ee(e, "click", sl)
      ], u = !0);
    },
    p(o, [h]) {
      (!a || h & /*accept_file_types*/
      8192) && k(
        e,
        "accept",
        /*accept_file_types*/
        o[13]
      ), (!a || h & /*file_count*/
      32 && l !== (l = /*file_count*/
      o[5] === "multiple" || void 0)) && (e.multiple = l), (!a || h & /*file_count*/
      32 && t !== (t = /*file_count*/
      o[5] === "directory" || void 0)) && k(e, "webkitdirectory", t), (!a || h & /*file_count*/
      32 && n !== (n = /*file_count*/
      o[5] === "directory" || void 0)) && k(e, "mozdirectory", n), (!a || h & /*label*/
      1 && f !== (f = /*label*/
      o[0] + "-upload-button")) && k(e, "data-testid", f);
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
      33554563 && (g.$$scope = { dirty: h, ctx: o }), c.$set(g);
    },
    i(o) {
      a || (we(c.$$.fragment, o), a = !0);
    },
    o(o) {
      ke(c.$$.fragment, o), a = !1;
    },
    d(o) {
      o && (X(e), X(r)), i[24](null), Ve(c, o), u = !1, ge(s);
    }
  };
}
function al(i) {
  console.log("drag over"), i.preventDefault(), i.stopPropagation();
}
function sl(i) {
  const e = i.target;
  e.value && (e.value = "");
}
function ul(i, e, l) {
  let { $$slots: t = {}, $$scope: n } = e;
  var f = this && this.__awaiter || function(_, v, z, w) {
    function F(D) {
      return D instanceof z ? D : new z(function(q) {
        q(D);
      });
    }
    return new (z || (z = Promise))(function(D, q) {
      function Q(O) {
        try {
          ne(w.next(O));
        } catch (te) {
          q(te);
        }
      }
      function ze(O) {
        try {
          ne(w.throw(O));
        } catch (te) {
          q(te);
        }
      }
      function ne(O) {
        O.done ? D(O.value) : F(O.value).then(Q, ze);
      }
      ne((w = w.apply(_, v || [])).next());
    });
  };
  let { elem_id: r = "" } = e, { elem_classes: c = [] } = e, { visible: a = !0 } = e, { loading_message: u } = e, { label: s } = e, { oldLabel: o } = e, { value: h } = e, { file_count: g } = e, { file_types: L = [] } = e, { root: S } = e, { size: B = "lg" } = e, { icon: m = null } = e, { scale: R = 1 } = e, { min_width: A = void 0 } = e, { variant: W = "secondary" } = e, { disabled: N = !1 } = e, { max_file_size: I = null } = e, { upload: J } = e;
  const y = il();
  let U, K;
  L == null ? K = null : (L = L.map((_) => _.startsWith(".") ? _ : _ + "/*"), K = L.join(", "));
  function ie() {
    y("click"), U.click();
  }
  function d(_) {
    return f(this, void 0, void 0, function* () {
      var v;
      let z = Array.from(_);
      if (!_.length)
        return;
      g === "single" && (z = [_[0]]);
      let w = yield je(z);
      yield ll();
      try {
        w = (v = yield J(w, S, void 0, I ?? 1 / 0)) === null || v === void 0 ? void 0 : v.filter((F) => F !== null);
      } catch (F) {
        y("error", F.message);
        return;
      }
      l(1, h = g === "single" ? w == null ? void 0 : w[0] : w), y("change", h), y("upload", h);
    });
  }
  function j(_) {
    return f(this, void 0, void 0, function* () {
      const v = _.target;
      v.files && (l(17, o = s), l(0, s = typeof u < "u" ? u : o), y("labelChange", s), yield d(v.files), l(0, s = o), y("labelChange", s));
    });
  }
  function G(_) {
    return f(this, void 0, void 0, function* () {
      var v;
      console.log({ min_width: A }), console.log({ scale: R }), console.log({ size: B }), console.log("drop");
      const z = _;
      z.preventDefault();
      const w = (v = z.dataTransfer) === null || v === void 0 ? void 0 : v.files;
      w && (l(17, o = s), l(0, s = typeof u < "u" ? u : o), y("labelChange", s), yield d(w), l(0, s = o), y("labelChange", s));
    });
  }
  function M(_) {
    Je[_ ? "unshift" : "push"](() => {
      U = _, l(12, U);
    });
  }
  return i.$$set = (_) => {
    "elem_id" in _ && l(2, r = _.elem_id), "elem_classes" in _ && l(3, c = _.elem_classes), "visible" in _ && l(4, a = _.visible), "loading_message" in _ && l(19, u = _.loading_message), "label" in _ && l(0, s = _.label), "oldLabel" in _ && l(17, o = _.oldLabel), "value" in _ && l(1, h = _.value), "file_count" in _ && l(5, g = _.file_count), "file_types" in _ && l(18, L = _.file_types), "root" in _ && l(20, S = _.root), "size" in _ && l(6, B = _.size), "icon" in _ && l(7, m = _.icon), "scale" in _ && l(8, R = _.scale), "min_width" in _ && l(9, A = _.min_width), "variant" in _ && l(10, W = _.variant), "disabled" in _ && l(11, N = _.disabled), "max_file_size" in _ && l(21, I = _.max_file_size), "upload" in _ && l(22, J = _.upload), "$$scope" in _ && l(25, n = _.$$scope);
  }, [
    s,
    h,
    r,
    c,
    a,
    g,
    B,
    m,
    R,
    A,
    W,
    N,
    U,
    K,
    ie,
    j,
    G,
    o,
    L,
    u,
    S,
    I,
    J,
    t,
    M,
    n
  ];
}
class ol extends Me {
  constructor(e) {
    super(), Ze(this, e, ul, fl, pe, {
      elem_id: 2,
      elem_classes: 3,
      visible: 4,
      loading_message: 19,
      label: 0,
      oldLabel: 17,
      value: 1,
      file_count: 5,
      file_types: 18,
      root: 20,
      size: 6,
      icon: 7,
      scale: 8,
      min_width: 9,
      variant: 10,
      disabled: 11,
      max_file_size: 21,
      upload: 22
    });
  }
}
const {
  SvelteComponent: _l,
  create_component: cl,
  destroy_component: dl,
  detach: rl,
  init: ml,
  insert: hl,
  mount_component: bl,
  safe_not_equal: gl,
  set_data: vl,
  text: wl,
  transition_in: kl,
  transition_out: zl
} = window.__gradio__svelte__internal;
function Cl(i) {
  let e = (
    /*label*/
    (i[0] ? (
      /*gradio*/
      i[15].i18n(
        /*label*/
        i[0]
      )
    ) : "") + ""
  ), l;
  return {
    c() {
      l = wl(e);
    },
    m(t, n) {
      hl(t, l, n);
    },
    p(t, n) {
      n & /*label, gradio*/
      32769 && e !== (e = /*label*/
      (t[0] ? (
        /*gradio*/
        t[15].i18n(
          /*label*/
          t[0]
        )
      ) : "") + "") && vl(l, e);
    },
    d(t) {
      t && rl(l);
    }
  };
}
function Ll(i) {
  let e, l;
  return e = new ol({
    props: {
      elem_id: (
        /*elem_id*/
        i[2]
      ),
      elem_classes: (
        /*elem_classes*/
        i[3]
      ),
      visible: (
        /*visible*/
        i[5]
      ),
      file_count: (
        /*file_count*/
        i[7]
      ),
      file_types: (
        /*file_types*/
        i[8]
      ),
      size: (
        /*size*/
        i[10]
      ),
      scale: (
        /*scale*/
        i[11]
      ),
      icon: (
        /*icon*/
        i[12]
      ),
      min_width: (
        /*min_width*/
        i[13]
      ),
      root: (
        /*root*/
        i[9]
      ),
      value: (
        /*value*/
        i[1]
      ),
      disabled: (
        /*disabled*/
        i[16]
      ),
      variant: (
        /*variant*/
        i[14]
      ),
      oldLabel: (
        /*oldLabel*/
        i[6]
      ),
      label: (
        /*label*/
        i[0]
      ),
      loading_message: (
        /*loading_message*/
        i[4]
      ),
      max_file_size: (
        /*gradio*/
        i[15].max_file_size
      ),
      upload: (
        /*gradio*/
        i[15].client.upload
      ),
      $$slots: { default: [Cl] },
      $$scope: { ctx: i }
    }
  }), e.$on(
    "click",
    /*click_handler*/
    i[20]
  ), e.$on(
    "change",
    /*change_handler*/
    i[21]
  ), e.$on(
    "upload",
    /*upload_handler*/
    i[22]
  ), e.$on(
    "labelChange",
    /*handleLabelChange*/
    i[18]
  ), e.$on(
    "error",
    /*error_handler*/
    i[23]
  ), {
    c() {
      cl(e.$$.fragment);
    },
    m(t, n) {
      bl(e, t, n), l = !0;
    },
    p(t, [n]) {
      const f = {};
      n & /*elem_id*/
      4 && (f.elem_id = /*elem_id*/
      t[2]), n & /*elem_classes*/
      8 && (f.elem_classes = /*elem_classes*/
      t[3]), n & /*visible*/
      32 && (f.visible = /*visible*/
      t[5]), n & /*file_count*/
      128 && (f.file_count = /*file_count*/
      t[7]), n & /*file_types*/
      256 && (f.file_types = /*file_types*/
      t[8]), n & /*size*/
      1024 && (f.size = /*size*/
      t[10]), n & /*scale*/
      2048 && (f.scale = /*scale*/
      t[11]), n & /*icon*/
      4096 && (f.icon = /*icon*/
      t[12]), n & /*min_width*/
      8192 && (f.min_width = /*min_width*/
      t[13]), n & /*root*/
      512 && (f.root = /*root*/
      t[9]), n & /*value*/
      2 && (f.value = /*value*/
      t[1]), n & /*disabled*/
      65536 && (f.disabled = /*disabled*/
      t[16]), n & /*variant*/
      16384 && (f.variant = /*variant*/
      t[14]), n & /*oldLabel*/
      64 && (f.oldLabel = /*oldLabel*/
      t[6]), n & /*label*/
      1 && (f.label = /*label*/
      t[0]), n & /*loading_message*/
      16 && (f.loading_message = /*loading_message*/
      t[4]), n & /*gradio*/
      32768 && (f.max_file_size = /*gradio*/
      t[15].max_file_size), n & /*gradio*/
      32768 && (f.upload = /*gradio*/
      t[15].client.upload), n & /*$$scope, label, gradio*/
      33587201 && (f.$$scope = { dirty: n, ctx: t }), e.$set(f);
    },
    i(t) {
      l || (kl(e.$$.fragment, t), l = !0);
    },
    o(t) {
      zl(e.$$.fragment, t), l = !1;
    },
    d(t) {
      dl(e, t);
    }
  };
}
function ql(i, e, l) {
  let t;
  var n = this && this.__awaiter || function(d, j, G, M) {
    function _(v) {
      return v instanceof G ? v : new G(function(z) {
        z(v);
      });
    }
    return new (G || (G = Promise))(function(v, z) {
      function w(q) {
        try {
          D(M.next(q));
        } catch (Q) {
          z(Q);
        }
      }
      function F(q) {
        try {
          D(M.throw(q));
        } catch (Q) {
          z(Q);
        }
      }
      function D(q) {
        q.done ? v(q.value) : _(q.value).then(w, F);
      }
      D((M = M.apply(d, j || [])).next());
    });
  };
  let { elem_id: f = "" } = e, { elem_classes: r = [] } = e, { loading_message: c = "fr" } = e, { visible: a = !0 } = e, { label: u } = e, { oldLabel: s } = e, { value: o } = e, { file_count: h } = e, { file_types: g = [] } = e, { root: L } = e, { size: S = "lg" } = e, { scale: B = null } = e, { icon: m = null } = e, { min_width: R = void 0 } = e, { variant: A = "secondary" } = e, { gradio: W } = e, { interactive: N } = e;
  function I(d, j) {
    return n(this, void 0, void 0, function* () {
      l(1, o = d), console.log("handle_event", d, j), W.dispatch(j);
    });
  }
  function J(d) {
    l(0, u = d.detail);
  }
  const y = () => W.dispatch("click"), U = ({ detail: d }) => I(d, "change"), K = ({ detail: d }) => I(d, "upload"), ie = ({ detail: d }) => {
    W.dispatch("error", d);
  };
  return i.$$set = (d) => {
    "elem_id" in d && l(2, f = d.elem_id), "elem_classes" in d && l(3, r = d.elem_classes), "loading_message" in d && l(4, c = d.loading_message), "visible" in d && l(5, a = d.visible), "label" in d && l(0, u = d.label), "oldLabel" in d && l(6, s = d.oldLabel), "value" in d && l(1, o = d.value), "file_count" in d && l(7, h = d.file_count), "file_types" in d && l(8, g = d.file_types), "root" in d && l(9, L = d.root), "size" in d && l(10, S = d.size), "scale" in d && l(11, B = d.scale), "icon" in d && l(12, m = d.icon), "min_width" in d && l(13, R = d.min_width), "variant" in d && l(14, A = d.variant), "gradio" in d && l(15, W = d.gradio), "interactive" in d && l(19, N = d.interactive);
  }, i.$$.update = () => {
    i.$$.dirty & /*interactive*/
    524288 && l(16, t = !N);
  }, [
    u,
    o,
    f,
    r,
    c,
    a,
    s,
    h,
    g,
    L,
    S,
    B,
    m,
    R,
    A,
    W,
    t,
    I,
    J,
    N,
    y,
    U,
    K,
    ie
  ];
}
class Sl extends _l {
  constructor(e) {
    super(), ml(this, e, ql, Ll, gl, {
      elem_id: 2,
      elem_classes: 3,
      loading_message: 4,
      visible: 5,
      label: 0,
      oldLabel: 6,
      value: 1,
      file_count: 7,
      file_types: 8,
      root: 9,
      size: 10,
      scale: 11,
      icon: 12,
      min_width: 13,
      variant: 14,
      gradio: 15,
      interactive: 19
    });
  }
}
export {
  ol as BaseUploadButton,
  Sl as default
};
