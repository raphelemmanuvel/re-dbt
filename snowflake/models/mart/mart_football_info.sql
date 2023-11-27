with
  qryMatches as (
    SELECT * FROM {{ ref('stg_football_matches') }} where league = 'Barclays Premier League'
    ),
  qryRankings as (
    SELECT * FROM {{ ref('stg_global_rankings') }} where league = 'Barclays Premier League'
  ),

  qryFinal as (
    select
      qryMatches.season,
      qryMatches.date,
      qryMatches.league,
      qryMatches.team1,
      qryMatches.team2,
      team_one.rank as team1_rank,
      team_two.rank as team2_rank
    from
      qryMatches join
      qryRankings as team_one on
        (qryMatches.team1 = team_one.name) join
      qryRankings as team_two on
        (qryMatches.team2 = team_two.name)
  )

select * from qryFinal
