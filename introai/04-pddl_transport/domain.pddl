(define (domain transport)
    (:predicates
        (car ?car)
        (box ?box)
        (place ?place)
        (at ?obj ?loc)
        (empty ?car)
    )
;; action 1
(:action load
    :parameters (?box  ?car ?place)
    :precondition (and (car ?car)( box ?box) (place ?place)(at ?car ?place) (empty ?car) (at ?box ?place))
    :effect (and (not (empty ?car)) (not(at ?box ?place)) (at ?box ?car))    
)
    
;; action 2
(:action unload
    :parameters (?box  ?car ?place)
    :precondition (and (car ?car)( box ?box) (place ?place)(at ?car ?place) (at ?box ?car) )
    :effect (and (empty ?car) (not(at ?box ?car)) (at ?box ?place))
)
    
    

;; action 3
(:action move
    :parameters (?car ?place_origin ?place_destination)
    :precondition (and (car ?car)(place ?place_origin)(place ?place_destination)(at ?car ?place_origin))
    :effect (and (not(at ?car ?place_origin)) (at ?car ?place_destination))
    
)
)