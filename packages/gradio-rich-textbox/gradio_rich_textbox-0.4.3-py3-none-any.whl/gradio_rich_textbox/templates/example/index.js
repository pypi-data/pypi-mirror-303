const {
  SvelteComponent: y,
  add_iframe_resize_listener: b,
  add_render_callback: m,
  append_hydration: v,
  attr: w,
  binding_callbacks: z,
  children: k,
  claim_element: p,
  claim_text: E,
  detach: o,
  element: S,
  init: q,
  insert_hydration: C,
  noop: f,
  safe_not_equal: D,
  set_data: I,
  text: M,
  toggle_class: _
} = window.__gradio__svelte__internal, { onMount: P } = window.__gradio__svelte__internal;
function V(l) {
  let e, i, r;
  return {
    c() {
      e = S("div"), i = M(
        /*value*/
        l[0]
      ), this.h();
    },
    l(t) {
      e = p(t, "DIV", { class: !0 });
      var n = k(e);
      i = E(
        n,
        /*value*/
        l[0]
      ), n.forEach(o), this.h();
    },
    h() {
      w(e, "class", "svelte-84cxb8"), m(() => (
        /*div_elementresize_handler*/
        l[5].call(e)
      )), _(
        e,
        "table",
        /*type*/
        l[1] === "table"
      ), _(
        e,
        "gallery",
        /*type*/
        l[1] === "gallery"
      ), _(
        e,
        "selected",
        /*selected*/
        l[2]
      );
    },
    m(t, n) {
      C(t, e, n), v(e, i), r = b(
        e,
        /*div_elementresize_handler*/
        l[5].bind(e)
      ), l[6](e);
    },
    p(t, [n]) {
      n & /*value*/
      1 && I(
        i,
        /*value*/
        t[0]
      ), n & /*type*/
      2 && _(
        e,
        "table",
        /*type*/
        t[1] === "table"
      ), n & /*type*/
      2 && _(
        e,
        "gallery",
        /*type*/
        t[1] === "gallery"
      ), n & /*selected*/
      4 && _(
        e,
        "selected",
        /*selected*/
        t[2]
      );
    },
    i: f,
    o: f,
    d(t) {
      t && o(e), r(), l[6](null);
    }
  };
}
function W(l, e, i) {
  let { value: r } = e, { type: t } = e, { selected: n = !1 } = e, d, a;
  function u(s, c) {
    !s || !c || (a.style.setProperty("--local-text-width", `${c < 150 ? c : 200}px`), i(4, a.style.whiteSpace = "unset", a));
  }
  P(() => {
    u(a, d);
  });
  function h() {
    d = this.clientWidth, i(3, d);
  }
  function g(s) {
    z[s ? "unshift" : "push"](() => {
      a = s, i(4, a);
    });
  }
  return l.$$set = (s) => {
    "value" in s && i(0, r = s.value), "type" in s && i(1, t = s.type), "selected" in s && i(2, n = s.selected);
  }, [r, t, n, d, a, h, g];
}
class j extends y {
  constructor(e) {
    super(), q(this, e, W, V, D, { value: 0, type: 1, selected: 2 });
  }
}
export {
  j as default
};
