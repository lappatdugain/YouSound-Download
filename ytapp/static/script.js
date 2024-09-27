document.addEventListener("DOMContentLoaded", function () {
    // Fonction pour changer la visibilité des formulaires en fonction du choix dans la liste déroulante
    function basculerVisibiliteFormulaire() {
        var choix = document.getElementById("choice_langue").value;
        var elementsEnglish = document.getElementsByClassName("english");
        var elementsFrench = document.getElementsByClassName("french");

        if (choix === "english") {
            // Traiter chaque élément individuellement ou choisir l'élément que vous souhaitez manipuler
            for (var i = 0; i < elementsEnglish.length; i++) {
                elementsEnglish[i].style.display = "block";
            }
            for (var i = 0; i < elementsFrench.length; i++) {
                elementsFrench[i].style.display = "none";
            }
        } else if (choix === "french") {
            // Traiter chaque élément individuellement ou choisir l'élément que vous souhaitez manipuler
            for (var i = 0; i < elementsEnglish.length; i++) {
                elementsEnglish[i].style.display = "none";
            }
            for (var i = 0; i < elementsFrench.length; i++) {
                elementsFrench[i].style.display = "block";
            }
        }
    }

    // Ajouter un écouteur d'événements sur la liste déroulante pour déclencher la fonction lorsqu'elle change
    document.getElementById("choice_langue").addEventListener("change", basculerVisibiliteFormulaire);

    // Appeler la fonction pour définir l'état initial
    basculerVisibiliteFormulaire();
});
