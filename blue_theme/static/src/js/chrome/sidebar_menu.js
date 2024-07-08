odoo.define('blue_theme.SidebarMenu', [], function (require) {
    "use strict";

    // Función para guardar el estado del sidebar en el almacenamiento local
    function saveSidebarState(state) {
        localStorage.setItem('sidebarState', state);
    }

    // Función para obtener el estado del sidebar del almacenamiento local
    function getSidebarState() {
        return localStorage.getItem('sidebarState');
    }

    // Función para aplicar el estado del sidebar
    function applySidebarState(state) {
        if (state === 'open') {
            $("#openSidebar").hide();
            $("#closeSidebar").show();
            $("#sidebar_panel").show();
            var sidebarWidth = $("#sidebar_panel").outerWidth();
            $(".o_action_manager").css({'margin-left': sidebarWidth + 'px', 'transition': 'all .3s ease'});
            $(".top_heading").css({'margin-left': sidebarWidth + 'px', 'transition': 'all .3s ease', 'width': 'auto'});
            $(".o_main_navbar").addClass("small_nav");
        } else {
            $("#closeSidebar").hide();
            $("#openSidebar").show();
            $("#sidebar_panel").hide();
            $(".o_action_manager").css({'margin-left': '0px', 'transition': 'all .3s ease'});
            $(".top_heading").css({'margin-left': '0px', 'transition': 'all .3s ease', 'width': '100%'});
            $(".o_main_navbar").removeClass("small_nav");
        }
    }

    // Aplicar el estado guardado del sidebar al cargar la página
    $(document).ready(function () {
        var state = getSidebarState();
        if (state) {
            applySidebarState(state);
        }
    });

    // Efecto de alternancia del sidebar
    $(document).on("click", "#closeSidebar", function (event) {
        saveSidebarState('closed');
        applySidebarState('closed');
    });

    $(document).on("click", "#openSidebar", function (event) {
        saveSidebarState('open');
        applySidebarState('open');
    });

    $(document).on("click", ".sidebar a", function (event) {
        var menu = $(".sidebar a");
        var $this = $(this);
        var id = $this.data("id");
        $("header").removeClass().addClass(id);
        menu.removeClass("active");
        $this.addClass("active");
        // Cerrar el sidebar al hacer clic en un elemento del menú
        saveSidebarState('closed');
        applySidebarState('closed');
    });

    // Ajustar el sidebar en pantallas pequeñas
    $(window).on('resize', function () {
        if ($(window).width() < 768) {
            saveSidebarState('closed');
            applySidebarState('closed');
        }
    });

    // Cambiar iconos del menú cuando el sidebar está abierto/cerrado
    $(document).on("click", "#openSidebar, #closeSidebar", function (event) {
        if ($("#sidebar_panel").is(':visible')) {
            $(".sidebar a i").addClass('open-icon').removeClass('close-icon');
        } else {
            $(".sidebar a i").addClass('close-icon').removeClass('open-icon');
        }
    });
});
