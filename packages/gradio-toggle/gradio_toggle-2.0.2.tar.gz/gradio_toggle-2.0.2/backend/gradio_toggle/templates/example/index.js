const {
  SvelteComponent: o,
  append_hydration: r,
  attr: u,
  children: f,
  claim_element: g,
  claim_text: h,
  detach: _,
  element: v,
  init: m,
  insert_hydration: y,
  noop: d,
  safe_not_equal: b,
  set_data: w,
  text: S,
  toggle_class: c
} = window.__gradio__svelte__internal;
function E(n) {
  let e, a = (
    /*value*/
    (n[0] !== null ? (
      /*value*/
      n[0].toLocaleString()
    ) : "") + ""
  ), i;
  return {
    c() {
      e = v("div"), i = S(a), this.h();
    },
    l(t) {
      e = g(t, "DIV", { class: !0 });
      var l = f(e);
      i = h(l, a), l.forEach(_), this.h();
    },
    h() {
      u(e, "class", "svelte-1gecy8w"), c(
        e,
        "table",
        /*type*/
        n[1] === "table"
      ), c(
        e,
        "gallery",
        /*type*/
        n[1] === "gallery"
      ), c(
        e,
        "selected",
        /*selected*/
        n[2]
      );
    },
    m(t, l) {
      y(t, e, l), r(e, i);
    },
    p(t, [l]) {
      l & /*value*/
      1 && a !== (a = /*value*/
      (t[0] !== null ? (
        /*value*/
        t[0].toLocaleString()
      ) : "") + "") && w(i, a), l & /*type*/
      2 && c(
        e,
        "table",
        /*type*/
        t[1] === "table"
      ), l & /*type*/
      2 && c(
        e,
        "gallery",
        /*type*/
        t[1] === "gallery"
      ), l & /*selected*/
      4 && c(
        e,
        "selected",
        /*selected*/
        t[2]
      );
    },
    i: d,
    o: d,
    d(t) {
      t && _(e);
    }
  };
}
function L(n, e, a) {
  let { value: i } = e, { type: t } = e, { selected: l = !1 } = e;
  return n.$$set = (s) => {
    "value" in s && a(0, i = s.value), "type" in s && a(1, t = s.type), "selected" in s && a(2, l = s.selected);
  }, [i, t, l];
}
class q extends o {
  constructor(e) {
    super(), m(this, e, L, E, b, { value: 0, type: 1, selected: 2 });
  }
}
export {
  q as default
};
